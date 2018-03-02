from django.conf.urls import url
from .views import IndexView, DetailView, PostLikeView, SearchFormView
from django.contrib.auth.decorators import login_required

app_name = 'blog'

urlpatterns = [
    url(r'^$', login_required(IndexView.as_view()), name='index'),
    url(r'^search/$', login_required(SearchFormView.as_view()), name='search'),
    url(r'^(?P<slug>.*)/$', login_required(DetailView.as_view()), name='post'),
    url(r'^(?P<slug>.*)/like$', login_required(PostLikeView.as_view()), name='like'),


]
