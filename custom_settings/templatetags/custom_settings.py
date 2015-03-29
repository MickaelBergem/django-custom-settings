from django import template
from django.conf import settings

register = template.Library()


@register.assignment_tag
def settings_value(name):
    """ Returns the settings variable corresponding to `name`, and an empty string if there is no such variable """
    return getattr(settings, name, "")
