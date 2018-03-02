from django.conf.urls import url
from .views import PostListView
from rest_framework_swagger.views import get_swagger_view
from rest_framework_jwt.views import obtain_jwt_token

app_name = 'api'

schema_view = get_swagger_view(title='PostAPI')

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='api_list'),
    url(r'^token-auth/', obtain_jwt_token),
    url(r'^documentation/$', schema_view)
]