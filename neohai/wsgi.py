"""
WSGI config for neohai project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""
import dotenv
import os
from django.core.wsgi import get_wsgi_application

dotenv.read_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neohai.settings')

application = get_wsgi_application()
