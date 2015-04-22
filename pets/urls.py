from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from .api import AnimalList

router = routers.DefaultRouter()
router.register(r'animal', AnimalList)

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
