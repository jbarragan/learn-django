from django import template

register = template.Library()

def my_cut(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg, '')

@register.filter(name="my_cut2")
def my_cut2(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg, '')

register.filter("my_cut", my_cut)
