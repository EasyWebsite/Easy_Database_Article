from django.contrib import admin
from django.urls import path, include

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Easy_Database_User.settings")
django.setup()

from rest_framework.routers import DefaultRouter
from Article.views import *

router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
]
