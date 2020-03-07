from django.conf.urls import url, include
from .views import view_cart, add_to_cart, adjust_cart
from issues import urls as urls_issues

urlpatterns = [
    url(r'^$', view_cart, name='view_cart'),
    url(r'^add/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
    url(r'^adjust/(?P<id>\d+)', adjust_cart, name='adjust_cart'),
    url(r'^issues/', include(urls_issues)),
]