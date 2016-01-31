from django import template

register = template.Library()


@register.filter(name='addcss')
def addcss(value, arg):
    return value.as_widget(attrs={'class': arg})


@register.filter(name='lookup_permission_text')
def lookup_permission_text(d, key):
    return d[key][1]


@register.filter(name='lookup_permission_text2')
def lookup_permission_text(d, key):
    print d
    return d[key][1]


@register.filter(name='get_range')
def get_range(number):
    return range(number)