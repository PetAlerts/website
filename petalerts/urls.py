from django.conf.urls import url, include
from django.contrib import admin
import pets.urls

urlpatterns = [
    url(r'^', include(pets.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
