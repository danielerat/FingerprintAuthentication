from django import template
register = template.Library()

@register.filter
def gender_label(value):
    if value == 'M':
        return 'Male'
    elif value == 'F':
        return 'Female'
    else:
        return value