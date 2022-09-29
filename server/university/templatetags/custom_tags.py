from django import template
from university.models import City, SiteSettings, Faculty
from typing import List

register = template.Library()

@register.simple_tag
def setting(name:str):
    return getattr(SiteSettings.load(),name,None)

@register.simple_tag
def faculties( amount:int = None ) -> List[Faculty] :
    return Faculty.objects.all()[:amount]

@register.simple_tag
def cities() -> List[City] :
    return City.object.all()