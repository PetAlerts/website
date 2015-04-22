from django.conf import settings
from django.conf.urls import url, include, static
from rest_framework import routers

from .api import AnimalList

router = routers.DefaultRouter()
router.register(r'animal', AnimalList)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)