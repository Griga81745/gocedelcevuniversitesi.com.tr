from django.contrib import admin

from . import models

admin.site.register(models.FAQ)
admin.site.register(models.Faculty)
admin.site.register(models.Area)
admin.site.register(models.Post)
admin.site.register(models.City)
admin.site.register(models.Request)
admin.site.register(models.SiteSettings)