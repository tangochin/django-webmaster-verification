"""
Source: http://datadesk.latimes.com/posts/2012/06/test-your-django-app-with-travisci/
Slightly modified by Nicolas Kuttler.
"""

import os
import sys
import argparse

from django.conf import settings


class QuickDjangoTest(object):
    """
    A quick way to run the Django test suite without a fully-configured project.

    Example usage:

        >>> QuickDjangoTest('app1', 'app2')

    Based on a script published by Lukasz Dziedzia at:
    http://stackoverflow.com/questions/3841725/how-to-launch-tests-for-django-reusable-app
    """
    DIRNAME = os.path.dirname(__file__)
    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.admin',

        'webmaster_verification'
    )
    WEBMASTER_VERIFICATION = {}

    def __init__(self, options, *args, **kwargs):
        self.apps = options.apps
        self.multicode = options.multicode
        self._tests()

    def _tests(self):
        """
        Fire up the Django test suite developed for version 1.2
        """
        settings.configure(
            DEBUG = True,
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': os.path.join(self.DIRNAME, 'database.db'),
                    'USER': '',
                    'PASSWORD': '',
                    'HOST': '',
                    'PORT': '',
                }
            },
            INSTALLED_APPS = self.INSTALLED_APPS,
            WEBMASTER_VERIFICATION = self._get_wv_config(),
            ROOT_URLCONF = 'test_project.urls',
            TEMPLATE_DIRS = (
                './test_project/templates/',
            ),
        )

        # Django 1.7
        import django
        if hasattr(django, 'setup'):
            django.setup()

        try:
            from django.test.simple import DjangoTestSuiteRunner
            failures = DjangoTestSuiteRunner().run_tests(self.apps,
                    verbosity=1)
            if failures:
                sys.exit(failures)
        except ImportError:
            # Django 1.8
            from django.test.runner import DiscoverRunner
            DiscoverRunner().run_tests(self.apps, verbosity=1)

    def _get_wv_config(self, key='default'):
        if self.multicode:
            conf = {
                'bing': 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF',
                'google': (
                    'ffffffffffffffff',
                    'aaaaaaaaaaaaaaaa',
                ),
                'majestic': (
                    'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF',
                    'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
                ),
                'yandex': (
                    'f0f0f0f0f0f0f0f0',
                    '1919191919191919',
                ),
                'alexa': (
                    '1234567890abcdefABCDEF12345',
                    '12345abcdef1234567890ABCDEF',
                ),
            }
        else:
            conf = {
                'bing': 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF',
                'google': 'ffffffffffffffff',
                'majestic': 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF',
                'yandex': 'f0f0f0f0f0f0f0f0',
                'alexa': '12345abcdef1234567890ABCDEF',
            }
        return conf


if __name__ == '__main__':
    """
    What do when the user hits this file from the shell.

    Example usage:

        $ python quicktest.py app1 app2

    """
    parser = argparse.ArgumentParser(
        usage="[args]",
        description="Run Django tests on the provided applications."
    )
    parser.add_argument('apps', nargs='+', type=str)
    parser.add_argument('--multicode', action="store_true",
                        help='run the multicode tests')
    options = parser.parse_args()
    QuickDjangoTest(options)