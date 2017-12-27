django-custom-settings
======================

Provides a very simple tag to load settings variables from Django templates.
If the variable doesn't exists, an empty string is returned.

.. image:: https://travis-ci.org/MickaelBergem/django-custom-settings.svg?branch=master
   :target: https://travis-ci.org/MickaelBergem/django-custom-settings

.. image:: https://coveralls.io/repos/github/MickaelBergem/django-custom-settings/badge.svg?branch=master
   :target: https://coveralls.io/github/MickaelBergem/django-custom-settings?branch=master

Install
-------

To install / update the module:

.. code:: bash

    pip install django-custom-settings-templatetag -U

Usage
-------

In your Django template, do the following :

.. code:: jinja2

    {% load custom_settings %}
    {% settings_value "CUSTOM_VAR_IN_SETTINGS" as CUSTOM_VAR %}
    {% if CUSTOM_VAR %}
      var={{ CUSTOM_VAR }}
    {% endif %}
