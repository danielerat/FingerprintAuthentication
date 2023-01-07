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
@register.filter
def health_class(value):
    if value == '1':
        return 'Class 1'
    elif value == '2':
        return 'Class 2'
    elif value == '3':
        return 'Class 3'
    elif value == '3':
        return 'Class 4'
    else:
        return value

@register.filter
def multiply(value, arg):
    return value * arg