from django.conf.urls import url, include
from .views import all_issues, all_bugs, issue_detail

urlpatterns = [
    url(r'^$', all_issues, name='issues'),
    url(r'^bugs/$', all_bugs, name='bugs'),
    url(r'^(?P<pk>\d+)/$', issue_detail, name='issue_detail'),
]