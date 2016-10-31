from django import template
from django.utils.translation import ugettext as _

register = template.Library()

@register.filter
def in_category(things, category):
    return things.filter(category=category)
@register.filter
def language(things, language_code):
    if language_code == "en":
        language = "English"
    else:
        language = "Українська"
    return things.filter(language=language)
