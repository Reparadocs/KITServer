from django.conf.urls import include, url
from rest_framework.authtoken import views as authviews
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^facebook/', views.FacebookLogin.as_view(), name='facebook'),
    url(r'^create/', views.CreateUser.as_view(), name='create'),
    url(r'^login/', authviews.obtain_auth_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)
