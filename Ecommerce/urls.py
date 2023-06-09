from django.contrib import admin
from django.urls import path, include

# for media file
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path('', include('Shop.urls')),
    path('account/', include('login.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings
                      .MEDIA_ROOT)