"""URL configuration for the mySite project.

This module defines the URL patterns for the project:
- Admin routes
- Includes the 'personal' app URL configuration
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('personal.urls')),  # personal app handles main pages
]
