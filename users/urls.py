from django.conf.urls import url
from .views import Login, logout

urlpatterns = [
    url(r'^login/', Login.as_view(), name='login'),
    url(r'^logout/', logout, name='logout')
]
