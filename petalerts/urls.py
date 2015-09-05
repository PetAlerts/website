from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns

import alerts.urls
import users.urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # Social Auth
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    url(r'^', include(users.urls, namespace='users')),
    url(r'^', include(alerts.urls, namespace='alerts')),
    url('', include('social.apps.django_app.urls', namespace='social')),
)