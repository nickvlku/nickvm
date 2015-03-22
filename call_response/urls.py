from django.conf.urls import url, patterns
from call_response.views import Greeting

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nickvm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'index/?$', 'call_response.views.index'),
    url(r'greeting/?$', Greeting.as_view()),

)
