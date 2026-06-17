from django.contrib import admin
from .models import Editor, Contact, Like, Comment

admin.site.register(Editor)
admin.site.register(Contact)
admin.site.register(Like)
admin.site.register(Comment)