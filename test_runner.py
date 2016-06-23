#!/usr/bin/env python
import sys

import django
from django.conf import settings
from django.test.runner import DiscoverRunner

settings.configure(
    DEBUG=True,
    DATABASES={'default': {'ENGINE': 'django.db.backends.sqlite3'}},
    ROOT_URLCONF='support_views.test_urls',
    INSTALLED_APPS=(
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.staticfiles',
    ),
    MIDDLEWARE_CLASSES=(
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
    ),
)

django.setup()
failures = DiscoverRunner(verbosity=1, failfast=True)\
        .run_tests(['support_views'])
if failures:
    sys.exit(failures)
