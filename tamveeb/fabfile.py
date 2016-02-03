import re
from StringIO import StringIO
import string
import os

from fabric import colors
from fabric.api import *
from fabric.contrib.console import confirm
from fabric.utils import indent

from django.utils.crypto import get_random_string

from hammer import __version__ as hammer_version
from hammer.vcs import Vcs

"""
    Usage:
        fab TARGET actions

    Actions:
        simple_deploy # Deploy updates without migrations.
            :arg id Identifier to pass to vcs update command.
            :arg silent If true doesn't show confirms.

        offline_deploy # Deploy updates with migrations with server restart.
            :arg id Identifier to pass to vcs update command.
            :arg silent If true doesn't show confirms.

        online_deploy # Deploy updates with migrations without server restart.
            :arg id Identifier to pass to vcs update command.
            :arg silent If true doesn't show confirms.

        version # Get the version deployed to target.
        update_requirements # Perform pip install -r requirements/production.txt

        stop_server # Stop the remote server service.
        start_server # Start the remote server service.
        restart_server # Restart the remote server service.

        migrate_diff # Get the status of migrations needed when upgrading target to the specified version.
            :arg id Identifier of revision to check against.
"""

# Ensure that we have expected version of the tg-hammer package installed
assert hammer_version == '0.0.5', "tg-hammer==0.0.5 is required"
vcs = Vcs.init(project_root=os.path.dirname(os.path.dirname(__file__)), use_sudo=True)

LOCAL_SETTINGS = """from settings.${target} import *

SECRET_KEY = '${secret_key}'

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME': 'tamveeb',
        'USER': 'tamveeb',
        'PASSWORD': '${db_password}',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
"""



""" TARGETS """


# Use  .ssh/config  so that you can use hosts defined there.
env.use_ssh_config = True


def defaults():
    env.venv_name = 'venv'
    env.confirm_required = True
    env.code_dir = '/'

    env.nginx_conf = 'nginx.conf'
    env.target = 'staging'

    env.service_name = ["gunicorn-tamveeb", ]
    env.code_dir = '/srv/tamveeb'

@task
def test():
    defaults()
    env.hosts = ['meeskoor.ee']
    env.tag = 'tamveeb-test'

@task
def live():
    raise NotImplemented('TODO: live host not configured')
    defaults()
    env.hosts = ['meeskoor.ee']
    env.tag = 'tamveeb-live'


@task
def staging():
    return test()

@task
def production():
    return live()


""" FUNCTIONS """


@task
def show_log(commit_id=None):
    """ List revisions to apply/unapply when updating to given revision.
        When no revision is given, it default to the head of current branch.
        Returns False when there is nothing to apply/unapply. otherwise revset of revisions that will be applied or
        unapplied (this can be passed to `hg|git status` to see which files changed for example).
    """
    result = vcs.deployment_list(commit_id)

    if 'message' in result:
        print(result['message'])
        return False

    elif 'forwards' in result:
        print("Revisions to apply:")
        print(indent(result['forwards']))

    elif 'backwards' in result:
        print("Revisions to rollback:")
        print(indent(result['backwards']))

    return result['revset']


@task
def migrate_diff(id=None, revset=None, silent=False):
    """ Check for migrations needed when updating to the given revision. """
    require('code_dir')

    # Exactly one of id and revset must be given
    assert (id or revset) and not (id and revset)

    # no revset given, calculate it by using deployment_list
    if not revset:
        result = vcs.deployment_list(id)

        if 'revset' not in result:
            print(result['message'])
            abort('Nothing to do')

        else:
            revset = result['revset']

    # Pull out migrations
    migrations = vcs.changed_files(revset, "\/(?P<model>\w+)\/migrations\/(?P<migration>.+)")

    if not silent and migrations:
        print "Found %d migrations." % len(migrations)
        print indent(migrations)

    return migrations


@task
def update_requirements(reqs_type='production'):
    """ Install the required packages from the requirements file using pip """
    require('hosts')
    require('code_dir')

    with cd(env.code_dir), prefix('. venv/bin/activate'):
        sudo('pip install -r requirements/%s.txt' % reqs_type)


def migrate(silent=False):
    """ Preform migrations on the database. """

    if not silent:
        request_confirm("migrate")

    management_cmd("migrate --noinput")


@task
def version():
    """ Get current target version hash. """
    require('hosts')
    require('code_dir')
    require('tag')

    print "Target %s version: %s" % (env.tag, colors.yellow(vcs.version()))


@task
def deploy(id=None, silent=False, force=False):
    """ Perform an automatic deploy to the target requested. """
    require('hosts')
    require('code_dir')

    # Ask for sudo at the begginning so we don't fail during deployment because of wrong pass
    if not sudo('whoami'):
        abort('Failed to elevate to root')
        return

    # Show log of changes, return if nothing to do
    revset = show_log(id)
    if not revset and not force:
        return

    # See if we have any requirements changes
    requirements_changes = force or vcs.changed_files(revset, r' requirements/')
    if requirements_changes:
        print colors.yellow("Will update requirements (and do migrations):")
        print indent(requirements_changes)

    # See if we have any changes to migrations between the revisions we're applying
    migrations = force or migrate_diff(revset=revset, silent=True)
    if migrations:
        print colors.yellow("Will apply %d migrations:" % len(migrations))
        print indent(migrations)

    # see if nginx conf has changed
    if vcs.changed_files(revset, r' deploy/%s' % env.nginx_conf):
        print colors.red("Warning: Nginx configuration change detected, also run: `fab %target% nginx_update`")

    if not silent:
        request_confirm("deploy")

    vcs.update(id)
    if requirements_changes:
        update_requirements()
    if migrations or requirements_changes:
        migrate(silent=True)

    collectstatic()

    restart_server(silent=True)

    # Run deploy systemchecks
    check()


@task
def simple_deploy(id=None, silent=False):
    """ Perform a simple deploy to the target requested. """
    require('hosts')
    require('code_dir')

    # Show log of changes, return if nothing to do
    revset = show_log(id)
    if not revset:
        return

    migrations = migrate_diff(revset=revset, silent=True)
    if migrations:
        msg = "Found %d migrations; are you sure you want to continue with simple deploy?" % len(migrations)
        if not confirm(colors.yellow(msg), False):
            abort('Deployment aborted.')

    if not silent:
        request_confirm("simple_deploy")

    vcs.update(id)
    collectstatic()
    restart_server(silent=True)


@task
def online_deploy(id=None, silent=False):
    """ Perform an online deploy to the target requested. """
    require('hosts')
    require('code_dir')

    # Show log of changes, return if nothing to do
    revset = show_log(id)
    if not revset:
        return

    migrations = migrate_diff(revset=revset, silent=True)
    if migrations:
        print colors.yellow("Will apply %d migrations:" % len(migrations))
        print indent(migrations)

    if not silent:
        request_confirm("online_deploy")

    vcs.update(id)
    migrate(silent=True)
    collectstatic()
    restart_server(silent=True)


@task
def offline_deploy(id=None, silent=False):
    """ Perform an offline deploy to the target requested. """
    require('hosts')
    require('code_dir')

    # Show log of changes, return if nothing to do
    revset = show_log(id)
    if not revset:
        return

    migrations = migrate_diff(revset=revset, silent=True)
    if migrations:
        print colors.yellow("Will apply %d migrations:" % len(migrations))
        print indent(migrations)

    if not silent:
        request_confirm("offline_deploy")

    stop_server(silent=True)
    vcs.update(id)
    migrate(silent=True)
    collectstatic()
    start_server(silent=True)


@task
def setup_server():
    require('hosts')
    require('code_dir')
    require('nginx_conf')

    # Clone code repository
    vcs.clone()

    # Create password for DB, secret key and the local settings
    db_password = generate_password()
    secret_key = generate_password()
    local_settings = string.Template(LOCAL_SETTINGS).substitute(db_password=db_password, secret_key=secret_key, target=env.target)

    # Create database
    sudo('echo "CREATE DATABASE tamveeb; '
         '      CREATE USER tamveeb WITH password \'%s\'; '
         '      GRANT ALL PRIVILEGES ON DATABASE tamveeb to tamveeb;" '
         '| su -c psql postgres' % db_password)

    # Create virtualenv and install dependencies
    with cd(env.code_dir):
        sudo('virtualenv -p python3.4 venv')
    update_requirements()

    # Upload local settings
    put(local_path=StringIO(local_settings), remote_path=env.code_dir + '/tamveeb/settings/local.py', use_sudo=True)

    # Create necessary dirs, with correct permissions
    mkdir_wwwdata('/var/log/tamveeb/')
    with cd(env.code_dir + '/tamveeb'), prefix('. ../venv/bin/activate'):
        mkdir_wwwdata('assets/CACHE/')
        mkdir_wwwdata('media/')

    # migrations, collectstatic
    management_cmd('migrate')
    collectstatic()

    # Ensure any and all created log files are owned by the www-data user
    sudo('chown -R www-data:www-data /var/log/tamveeb/')

    # Copy logrotate, nginx and gunicorn confs
    with cd(env.code_dir):
        sudo('cp deploy/logrotate.conf /etc/logrotate.d/tamveeb')
        sudo('cp deploy/%s /etc/nginx/sites-enabled/tamveeb' % env.nginx_conf)
        sudo('cp deploy/gunicorn.conf /etc/init/gunicorn-tamveeb.conf')
    

    # (Re)start services
    start_server(silent=True)

    # Run deploy systemchecks
    check()

    # Restart nginx
    sudo('service nginx restart')


@task
def nginx_update():
    require('code_dir')
    require('nginx_conf')

    # Update nginx config
    with cd(env.code_dir):
        sudo('cp deploy/%s /etc/nginx/sites-enabled/tamveeb' % env.nginx_conf)

    sudo('service nginx restart')


""" SERVER COMMANDS """


@task
def stop_server(silent=False):
    if not silent:
        request_confirm("stop_server")

    require('service_name')
    require('code_dir')

    service(env.service_name, "stop")


@task
def start_server(silent=False):
    if not silent:
        request_confirm("start_server")

    require('service_name')
    require('code_dir')
    service(env.service_name, "start")


@task
def restart_server(silent=False):
    if not silent:
        request_confirm("restart_server")

    require('service_name')
    require('code_dir')
    service(env.service_name, "restart")


@task
def management_cmd(cmd):
    """ Perform a management command on the target. """

    require('hosts')
    require('code_dir')

    sudo("cd %s ;"
         ". ./venv/bin/activate ; "
         "cd tamveeb ; "
         "python manage.py %s" % (env.code_dir, cmd))


@task
def check():
    """ Perform Django's deploy systemchecks. """
    require('hosts')
    require('code_dir')

    management_cmd('check --deploy')


""" HELPERS """


def service(names, cmd):
    if not isinstance(names, (list, tuple)):
        names = [names, ]

    for name in names:
        full_cmd = "service %s %s" % (name, cmd)

        try:
            sudo(full_cmd, warn_only=True)

        except Exception as e:
            print('Failed: %s', full_cmd)
            print(e)


@task
def repo_type():
    require('code_dir')

    try:
        print("Current project is using: `%s`" % colors.green(vcs.NAME))

    except EnvironmentError:
        print("Current project is using: `%s`" % colors.red('NO VCS'))


def collectstatic():
    with cd(env.code_dir + '/tamveeb'):
        sudo('bower install --production --allow-root')

    management_cmd('collectstatic --noinput')


def mkdir_wwwdata(path):
    # Creates directory and makes www-data its owner
    sudo('mkdir -p ' + path)
    sudo('chown www-data:www-data ' + path)


def request_confirm(tag):
    require('confirm_required')

    if env.confirm_required:
        if not confirm("Are you sure you want to run task: %s on servers %s?" % (tag, env.hosts)):
            abort('Deployment aborted.')


def generate_password(length=50):
    # Similar to Django's charset but avoids $ to avoid accidential shell variable expansion
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#%^&*(-_=+)'
    return get_random_string(length, chars)
