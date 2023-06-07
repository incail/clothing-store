"""
WSGI config for store project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.insert(0, '/home/storeclo/store')
sys.path.insert(0, '/home/storeclo/store/store')
sys.path.insert(1, '/home/storeclo/virtualenv/store/3.9/lib/python3.9/site-packages')

os.environ["DJANGO_SETTINGS_MODULE"] = "store.settings"

application = get_wsgi_application()
