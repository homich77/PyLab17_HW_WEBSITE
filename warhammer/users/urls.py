from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.login_view),
    url(r'^logout/$', views.logout),
    url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    url(r'^userlist/$', views.UserListView.as_view(), name='userlist')
        ]
