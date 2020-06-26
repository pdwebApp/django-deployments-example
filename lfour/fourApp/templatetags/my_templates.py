from django import template
register = template.Library()


@register.filter(name='cuts')
#This cuts out all values of arg from the string
def cut(value,arg):
    return value.replace(arg,'')

# register.filter('cut',cut)
# We can register filter in both ways
