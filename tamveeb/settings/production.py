from settings.staging import *


ALLOWED_HOSTS = ['185.7.254.130', 'meeskoor.ee', 'www.meeskoor.ee']

# Static site url, used when we need absolute url but lack request object, e.g. in email sending.
SITE_URL = 'http://meeskoor.ee/'

EMAIL_HOST_PASSWORD = 'TODO (api key)'

RAVEN_CONFIG['dsn'] = 'https://TODO@sentry.thorgate.eu/TODO',

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tamveeb',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
