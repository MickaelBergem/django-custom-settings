from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def settings_value(name):
    """
    Return the settings variable corresponding to `name`, or an empty string if
    there is no such variable.
    """
    return getattr(settings, name, "")
