from django import template

register = template.Library()

@register.filter
def list_sum(value):
    return sum(value)