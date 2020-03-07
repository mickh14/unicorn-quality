from django.conf.urls import url
from .views import do_search, issue_filter, bug_done, feature_done

urlpatterns = [
    url(r'^$', do_search, name='search'),
    url(r'^issue_filter/$', issue_filter, name='issue_filter'),
    url(r'^bug_done/$', bug_done, name='bug_done'),
    url(r'^feature_done/$', feature_done, name='feature_done'),
]