
"""warehouse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from products import views
#from views import index, contact
#from production import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^production/', include('production.urls'), name='production'),
    url(r'^users/', include('users.urls'), name='users'),
    url(r'^reports/', include('reports.urls'), name='reports'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^search/$',views.search, name='search'),
    url(r'^searchProvider/$',views.searchProvider, name='searchProvider'),
    url(r'^searchContacts/$',views.searchContacts, name='searchContacts'),
    url(r'^edit/(?P<id>\d+)/$',views.edit, name='edit_product'),
    url(r'^delete/(?P<id>\d+)/$',views.delete, name='delete_product'),
    url(r'^provider/$', views.provider, name='provider'),
    #url(r'^search2/$',views.search2.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)