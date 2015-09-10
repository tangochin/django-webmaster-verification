======
README
======

This application allows various webmaster tools to verify that a django site is
managed by you.

The only supported method of verification is by accessing a file on your
server.

Supported services:

- `Google Webmaster Tools <https://www.google.com/webmasters/tools/home>`_
- `Bing Webmaster Tools <https://ssl.bing.com/webmaster/Home/>`_
- `Yandex Webmaster Tools <http://webmaster.yandex.com/>`_
- `Majestic SEO <https://www.majesticseo.com>`_
- `Alexa <http://www.alexa.com>`_

.. image:: https://api.travis-ci.org/whyflyru/django-webmaster-verification.png
  :target: https://travis-ci.org/whyflyru/django-webmaster-verification

Usage
=====

Get ``django-webmaster-verification`` into your python path::

    pip install django-webmaster-verification

Add ``webmaster_verification`` to your INSTALLED_APPS in settings.py::

    INSTALLED_APPS = (
        ...,
        'webmaster_verification',
        ...,
    )

Add ``webmaster_verification`` to your root urlconf (urls.py)::

    urlpatterns = patterns('',
        ...,
        url(r'', include('webmaster_verification.urls')),
        ...,
    )

Add settings just as::

    WEBMASTER_VERIFICATION = {
        'bing': '<bing verification code>',
        'google': '<google verification code>',
        'majestic': '<majestic verification code>',
        'yandex': '<yandex verification code>',
        'alexa': '<alexa verification code>',
    }

The codes are alphanumeric and don't include suffixes like 'html', e.g.
``847e1f379a99c28a`` for google, not ``847e1f379a99c28a.html``.

Multiple codes are supported as well, except for bing::

    WEBMASTER_VERIFICATION = {
        'bing': '<bing verification code>',
        'google': (
                '<google verification code 1>',
                '<google verification code 2>',
        ),
        'majestic': (
                '<majestic verification code 1>',
                '<majestic verification code 2>',
        ),
        'yandex': (
                '<yandex verification code 1>',
                '<yandex verification code 2>',
        ),
        'alexa': (
                '<alexa verification code 1>',
                '<alexa verification code 2>',
        ),
    }

Notes
-----

Python 2.6 users will have to install argparse and importlib manually. I'm
too lazy to add that logic to the setup script right now.

As **Bing** always accesses the same verification file I'm not sure if it's
possible to support more than one code for it. Please let me know if yes, and
how, as I don't really use their tools.

For **Yandex** only the `.txt` file method is supported, but adding support for
`.html` should be trivial if you need it.

The **Alexa** codes I saw all had a length of 27 characters, so that's what this
app assumes is used. Please let me know if your codes differ and I need to
modify the app.

Changelog
=========

0.2.4 (2015-02-26)
------------------
- Add Django 1.8 (beta1) support and drop 1.5 tests

0.2.3 (2014-04-13)
------------------
- Django 1.7 (beta1) support

0.2.2 (2014-01-12)
------------------
- Django 1.6 support
- Removed Python 2.5 testing

0.2.1 (2013-03-25)
------------------
- Add alexa support
- Refactor the test project to use a different structure

0.2 (2013-02-16)
----------------
- Python 3.2 support
- Integrate testing with travis

0.1.10 (2012-12-21)
-------------------
- Fix test errors when running from a real project

0.1.9 (2012-12-19)
------------------
- Pypi updates

0.1.8 (2012-12-19)
------------------
- Yandex Webmaster Tools support added.

0.1.7 (2012-05-07)
------------------
- Bugfix for multiple verification codes for one provider.
