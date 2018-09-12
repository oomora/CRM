__author__ = 'oscarmora'
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from production import views
#from views import ActivityCreate

urlpatterns = [
    #url(r'^create/$', views.ActivityCreate, name='activityCreate'),
    url(r'^create/$', views.ActivityCreate.as_view(), name='activityCreate'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)