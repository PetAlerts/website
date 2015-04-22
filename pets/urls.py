from django.conf.urls import url, include
from rest_framework import routers
import api
import views

router = routers.DefaultRouter()
router.register(r'animal', api.AnimalList)

urlpatterns = [
    url(r'^', views.Home.as_view(), name='home'),
    url(r'^api/', include(router.urls)),
]
