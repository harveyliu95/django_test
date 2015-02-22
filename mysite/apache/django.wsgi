import os, sys

sys.path.append('F:\website-related\wamp\www\django_test\mysite')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()