# django-custom-settings

Provides a very simple tag to load settings variables from Django templates.
If the variable doesn't exists, an empty string is returned.

## Install

To install / update the module:

    pip install git+git://github.com/MickaelBergem/django-custom-settings.git -U

Or add `git+git://github.com/MickaelBergem/django-custom-settings.git` to your `requirements.txt`.

## Usage

In your Django tempalte, do the following :

    {% load custom_settings %}
    {% settings_value "CUSTOM_VAR_IN_SETTINGS" as CUSTOM_VAR %}
    {% if CUSTOM_VAR %}
      var={{ CUSTOM_VAR }}
    {% endif %}
