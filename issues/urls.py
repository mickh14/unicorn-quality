from django.conf.urls import url, include
from .views import all_issues, all_bugs, issue_detail, create_or_edit_issue

urlpatterns = [
    url(r'^$', all_issues, name='issues'),
    url(r'^bugs/$', all_bugs, name='bugs'),
    url(r'^(?P<pk>\d+)/$', issue_detail, name='issue_detail'),
    url(r'^new/$', create_or_edit_issue, name='new_issue'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_issue, name='edit_issue')
]