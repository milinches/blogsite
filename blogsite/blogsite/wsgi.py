"""
WSGI config for blogsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

# import os
#
# from django.core.wsgi import get_wsgi_application
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogsite.settings')
#
# application = get_wsgi_application()

import os
import sys

from django.core.wsgi import get_wsgi_application

path = "/home/ashish/Documents/Django/blog/blog_project/"
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'blogsite.settings'

application = get_wsgi_application()
