from django.conf.urls import include,url

from .views import *

urlpatterns = [
    url(r'^movies', IndexView.as_view(), name='index'),
    url('rest-auth/', include('rest_auth.urls')),
]
