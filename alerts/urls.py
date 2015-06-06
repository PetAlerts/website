from django.conf.urls import url, include
from rest_framework import routers
from alerts import api
from alerts import views

router = routers.DefaultRouter()
router.register(r'alert', api.AlertViewSet)

urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^alert/(?P<pk>[0-9]+)/$', views.AlertDetailView.as_view(), name='detail'),
    url(r'^create/$', views.AlertCreateView.as_view(), name='create'),
    url(r'^list/$', views.AlertList.as_view(), name='list'),
    url(r'^api/', include(router.urls)),
]
