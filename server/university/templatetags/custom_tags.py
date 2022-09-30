import markdown
from django import template
from django.utils.safestring import mark_safe
from university.models import City, Post, SiteSettings
from typing import List

register = template.Library()

@register.simple_tag
def setting(name:str):
    return getattr(SiteSettings.load(),name,None)

@register.simple_tag
def cities() -> List[City] :
    return City.object.all()

@register.simple_tag
def latest_posts(count:int=3) -> List[Post] :
    return Post.objects.order_by('id')[:count]

@register.filter(name='markdown')
def markdown_format(text:str) -> str :
    return mark_safe(markdown.markdown(text))