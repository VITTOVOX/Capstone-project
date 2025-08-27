"""Admin configuration for the polls/blog application.

This module registers models with the Django admin site so that
they can be managed through the built-in admin interface.
"""

from django.contrib import admin
from .models import Post, Question, Choice


# Register your models here with the admin site.
admin.site.register(Post)
admin.site.register(Question)
admin.site.register(Choice)
