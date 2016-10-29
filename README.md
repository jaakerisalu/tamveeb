# README for tamveeb

TODO: verify that the following info is correct:

 - Python:  3.4
 - DB:      PostgreSQL (locally SQLite)

## Setting up development

**Create virtualenv**

 `virtualenv --python=python3.4 venv`

 `. ./venv/bin/activate`

or if you use virtualenvwrapper

 `mkvirtualenv tamveeb`

 `workon tamveeb`

**Install dependencies**

 `pip install -r requirements/local.txt`\

**Switch to internal tamveeb dir**

 `cd tamveeb`

**Create local settings**

Create `settings/local.py` from `settings/local.py.example`

    cp settings/local.py.example settings/local.py

(now you can also open the project in PyCharm without running into issues due to missing virtualenv/settings)

**Apply database migrations**

 `python manage.py migrate`



## Running tests

Use `py.test` for running tests. It's configured to run the entire test-suite of the project by default.

    py.test

You can also use `--reuse-db` or `--nomigrations` flags to speed things up a bit. See also:
https://pytest-django.readthedocs.org/en/latest/index.html

### Coverage

You can also calculate tests coverage with `coverage run -m py.test && coverage html`,
the results will be in `cover/` directory.



This project includes Bower integration.
To install existing dependencies, run `bower install` in the inner project dir (where manage.py is).
To add a dependency, run `bower install <package-name> --save`.
Deploying with Fabric will ensure that all Bower dependencies are also installed in the server.
If you don't have Bower installed, you can get it by running `npm install -g bower`.


## Run with uWSGI

 `uwsgi --socket :8001 --module tamveeb.wsgi
