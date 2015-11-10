from django.conf.urls import include, url
from rest_framework.authtoken import views as authviews
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^create/', views.CreateContact.as_view(), name='create'),
    url(r'^list/', views.ContactList.as_view(), name='list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
