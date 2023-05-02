"""
WSGI config for wiki project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys

path = '/home/shen003/wiki-app'
if path not in sys.path:
    sys.path.insert(0, path)
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wiki.settings')

application = get_wsgi_application()
