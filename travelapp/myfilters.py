from django import template
from django.utils.safestring import mark_safe

import json

register = template.Library()

print('xxx')
@register.filter(name='tojson')
def json_dumps(data):
    return mark_safe(json.dumps(data))
