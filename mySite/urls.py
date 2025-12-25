"""URL configuration for the mySite project.

This module defines the URL patterns for the project:
- Admin routes
- Includes the 'personal' app URL configuration
"""

from django.contrib import admin
from django.urls import path, include
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('personal.urls')),  # personal app handles main pages
    path('accounts/', include('user_auth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
     path('admin/', admin.site.urls),
    path('accounts/', include('user_auth.urls')),

]
