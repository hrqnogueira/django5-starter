import os

from django.core.asgi import get_asgi_application

from decouple import config

environment = config('ENVIRONMENT', default='dev')
settings_path = "{{ project_name }}.settings.{}".format(environment)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_path)

application = get_asgi_application()
