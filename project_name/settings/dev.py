from {{ project_name }}.settings.base import *

INTERNAL_IPS = [
    '127.0.0.1'
]

INSTALLED_APPS += [
    'debug_toolbar',
    'django_extensions',
]

MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')