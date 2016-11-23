django-custom-settings
======================

Provides a very simple tag to load settings variables from Django templates.
If the variable doesn't exists, an empty string is returned.

Install
-------

To install / update the module:

.. code:: bash

    pip install django-custom-settings-templatetag -U

Usage
-------

In your Django tempalte, do the following :

.. code:: jinja2

    {% load custom_settings %}
    {% settings_value "CUSTOM_VAR_IN_SETTINGS" as CUSTOM_VAR %}
    {% if CUSTOM_VAR %}
      var={{ CUSTOM_VAR }}
    {% endif %}
