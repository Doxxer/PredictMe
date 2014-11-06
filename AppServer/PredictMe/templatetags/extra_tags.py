from django import template
register = template.Library()

@register.filter
def get(mapping, key):
  return mapping[key]