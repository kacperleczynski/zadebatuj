from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter
def has_group(user, group_name = 'judges'):
    group = Group.objects.get(name = group_name)
    return True if group in user.groups.all() else False
