from config.urls.base import *
from core.views import error404

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = urlpatterns + [
    url(r'^error404/$', error404),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
