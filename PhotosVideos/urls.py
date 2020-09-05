from django.conf.urls.static import static
from django.urls import path
from django.conf import settings

from django.conf.urls.static import static
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',views.index,name='home'),
    path('photos/',views.photo,name='photo'),
    path('videos/', views.video, name='video')

]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()
