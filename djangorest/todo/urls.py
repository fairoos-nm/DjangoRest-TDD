from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView


urlpatterns = {
    url(r'^auth/', include('rest_framework.urls',
                           namespace='rest_framework')),
    url(r'^todolists/$', CreateView.as_view(), name='todo_create'),
    url(r'^todolists/(?P<pk>[0-9]+)/$',
        DetailsView.as_view(), name='todo_details')
}

urlpatterns = format_suffix_patterns(urlpatterns)
