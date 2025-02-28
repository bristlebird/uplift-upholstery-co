"""
Template filter for calculating cart item sub-totals
"""
from django import template

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """ just returnt the product of the price by the quantity """
    return price * quantity
