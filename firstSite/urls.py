from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('firstApp.urls', namespace='firstApp')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # API urls
    url(r'^api/', include('firstApp.api.urls', namespace='posts-api')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          documnet_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          documnet_root=settings.STATIC_ROOT)
