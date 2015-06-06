from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
import alerts.urls

urlpatterns = [
    url(r'^', include(alerts.urls, namespace='alerts')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # Social Auth
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^login/', 'alerts.views.login'),
    url(r'^logout/', 'alerts.views.logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
