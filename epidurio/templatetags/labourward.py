"""
Template tags for the labour ward
"""
from django import template

register = template.Library()


@register.inclusion_tag('templatetags/labourward/ward_card.html')
def ward_card(room_name):
    return dict(room_name=room_name)
