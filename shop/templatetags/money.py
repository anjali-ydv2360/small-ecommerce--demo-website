from django import template

register = template.Library()


@register.filter
def dollars(cents):
    return f"{cents / 100:.2f}"