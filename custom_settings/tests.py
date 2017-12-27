from django.template import Context, Template
from django.test import TestCase


class CustomSettingsTests(TestCase):

    really_random_value = 'Really Random Value!'

    def test_render_variable(self):
        """ Test if a given variable is well rendered """
        # Override/Define a custom settings variable
        with self.settings(REALLY_RANDOM_VAR_BOUYAH=self.really_random_value):
            # Compute what the template will render
            rendered = Template(
                '{% load custom_settings %}'
                '{% settings_value "REALLY_RANDOM_VAR_BOUYAH" as REALLY_RANDOM_VAR %}'
                '{{ REALLY_RANDOM_VAR }}'
            ).render(Context())

        self.assertEqual(rendered, self.really_random_value)

    def test_render_unknown_variable(self):
        """ Test if an unknown variable is well rendered as an empty string """

        # Compute what the template will render
        rendered = Template(
            '{% load custom_settings %}'
            '{% settings_value "REALLY_RANDOM_VAR_BOUYAH_UNKNOWN" as REALLY_RANDOM_VAR %}'
            '{{ REALLY_RANDOM_VAR }}'
        ).render(Context())

        self.assertEqual(rendered, '')
