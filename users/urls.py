from django.conf.urls import url
from .views import Login, logout, UserSubscriptionsCreate, UserSubscriptionsList

urlpatterns = [
    url(r'^login/', Login.as_view(), name='login'),
    url(r'^logout/', logout, name='logout'),
    url(r'^subscriptions', UserSubscriptionsList.as_view(), name='subscriptions'),
    url(r'^subscribe', UserSubscriptionsCreate.as_view(), name='subscribe')
]
