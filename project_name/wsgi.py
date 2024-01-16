import os

from decouple import config
from django.core.wsgi import get_wsgi_application

environment = config('ENVIRONMENT', default='dev')
settings_module = '{{ project_name }}.settings.{}'.format(environment)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

application = get_wsgi_application()
