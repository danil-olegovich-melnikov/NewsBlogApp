from django.contrib import admin
from django.urls import path
from django.urls import include

from django.conf import settings
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('', schema_view),
    path('admin/', admin.site.urls),
    path('api/auth/', include('auth_user.urls')),
    path('api/', include("article.urls")),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
