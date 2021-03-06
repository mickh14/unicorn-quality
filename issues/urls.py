from django.conf.urls import url, include
from .views import all_issues, all_bugs, issue_detail, create_or_edit_issue, increment_vote, add_comment, pass_test

urlpatterns = [
    url(r'^$', all_issues, name='issues'),
    url(r'^bugs/$', all_bugs, name='bugs'),
    url(r'^(?P<pk>\d+)/$', issue_detail, name='issue_detail'),
    url(r'^(?P<pk>\d+)/vote/$', increment_vote, name='increment_vote'),
    url(r'^new/$', create_or_edit_issue, name='new_issue'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_issue, name='edit_issue'),
    url(r'^(?P<pk>\d+)/comment/$', add_comment, name='add_comment'),
    url(r'^(?P<pk>\d+)/pass/$', pass_test, name='pass_test')
]