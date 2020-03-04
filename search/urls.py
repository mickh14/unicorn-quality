from django.conf.urls import url
from .views import do_search, issue_filter

urlpatterns = [
    url(r'^$', do_search, name='search'),
    url(r'^issue_filter/$', issue_filter, name='issue_filter'),
]