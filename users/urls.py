from django.conf.urls import url
from .views import Login, logout, UserSubscriptionsCreate

urlpatterns = [
    url(r'^login/', Login.as_view(), name='login'),
    url(r'^logout/', logout, name='logout'),
    url(r'^subscriptions', UserSubscriptionsCreate.as_view(), name='subscriptions')
]
