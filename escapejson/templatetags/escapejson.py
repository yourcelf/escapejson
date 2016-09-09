import json

from django import template
from django.core.serializers.json import DjangoJSONEncoder
from django.utils import six
from django.utils.safestring import mark_safe
from ..escapejson import escapejson

register = template.Library()

@register.filter(name='escapejson')
def escapejson_filter(value):
    """
    Escape `value` to prevent </script> and unicode whitespace attacks. If
    `value` is not a string, JSON-encode it first.
    """
    if isinstance(value, six.string_types):
        string = value
    else:
        string = json.dumps(value, cls=DjangoJSONEncoder)
    return mark_safe(escapejson(string))
