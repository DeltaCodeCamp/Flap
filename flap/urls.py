from django.urls import path

from . import views

urlpatterns = [
path('signin', views.signin, name = "signin"),
path('special_second', views.special_second, name = "special_second"),
path('organization_second', views.organization_second, name = "organization_second"),
path('special', views.special, name = "special"),
path('organization', views.organization, name = "organization"),
path('events', views.events, name = "events"),
]
