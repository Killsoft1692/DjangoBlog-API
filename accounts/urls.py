from django.conf.urls import url
from accounts import views

app_name = "accounts"

urlpatterns = [
    url(r'^register/$', views.RegistrationFormView.as_view(), name='register'),
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^activate/(?P<id_>[0-9]+)/$', views.activate_user, name='activate'),
    url(r'^logout/$', views.logout_view, name='logout'),
]
