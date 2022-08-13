from django import template
register = template.Library()

@register.filter(name='get_replyes')
def get_replyes(dict,key):
    return dict.get(key)