from django.contrib import admin
from . import models

class TagAdmin(admin.ModelAdmin):
    fields = ['label']

class TagItemAdmin(admin.ModelAdmin):
    fields = ['tag', 'content_type', 'object_id']

admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.TagItem, TagItemAdmin)
