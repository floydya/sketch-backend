from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jet/', include('jet.urls', 'jet')),
]

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [path('rosetta/', include('rosetta.urls'))]

if 'des' in settings.INSTALLED_APPS:
    urlpatterns += [path('django-des/', include('des.urls'))]

if settings.DEBUG:
    urlpatterns += (
            static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +
            static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    )

    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns += [
            path('__debug__/', include(debug_toolbar.urls)),
        ]

API_VERSION = getattr(settings, 'API_VERSION', 1)
API_BASE_PREFIX = f'api/v{API_VERSION}/'

urlpatterns += [
    path(API_BASE_PREFIX, include([
        path('auth/', include('djoser.urls')),
        path('auth/', include('djoser.urls.authtoken')),
        path('auth/', include('djoser.urls.jwt')),
        path('', include('applications.accounts.api.urls')),
        path('', include('applications.notifications.api.urls')),
        path('', include('applications.transactions.api.urls')),
    ])),
]

urlpatterns += [
    # path('', TemplateView.as_view(template_name='index.html'), name="index"),
    # path('', include('applications.accounts.urls')),
]
