from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from push import views

urlpatterns = [
    url(r'^push/$', views.PushList.as_view()),
    url(r'^user/$', views.CreateUser.as_view()),
    url(r'^push/(?P<pk>[0-9]+)/$', views.PushDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)