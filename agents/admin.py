# agents/admin.py

from django.contrib import admin

from .models import (
    Customer,
    Project,
    Media,
    EditedContent,
    SocialMediaPost
)

admin.site.register(Customer)
admin.site.register(Project)
admin.site.register(Media)
admin.site.register(EditedContent)
admin.site.register(SocialMediaPost)