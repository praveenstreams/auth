from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.views import USerViewset

defaultone = DefaultRouter()
defaultone.register('user', USerViewset, basename='user')

urlpatterns = defaultone.urls+ [
    path('admin/', admin.site.urls),
]
