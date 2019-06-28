from django.urls import path, re_path

from . import views

urlpatterns = [
path('signin', views.signin, name = "signin"),
path('special_second', views.special_second, name = "special_second"),
path('organization_second', views.organization_second, name = "organization_second"),
path('special', views.special_, name = "special"),
path('organization', views.organization_, name = "organization"),
path('events', views.events_, name = "events"),
path('home', views.home, name = "home"),
re_path(r'^activation/(?P<redirection_code>[\w.@+-]+)/$', views.activation, name = "activation")
]
