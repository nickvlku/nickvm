from django.conf.urls import url, patterns
from call_response.views import Greeting, LeaveAMessage, CallStatus, CallAction, GreetingStatus

urlpatterns = patterns('',
    url(r'greeting/current$', GreetingStatus.as_view()),
    url(r'greeting/?$', Greeting.as_view()),
    url(r'message/?$', LeaveAMessage.as_view()),
    url(r'call$', CallAction.as_view()),
    url(r'call/(?P<call_id>.*)$', CallStatus.as_view())
)
