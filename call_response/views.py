from django.http.response import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

import twilio.twiml


@csrf_exempt
def index(request):
    resp = twilio.twiml.Response()
    resp.say("Hello Monkey")

    return HttpResponse(resp, content_type='application/xml')

class Greeting(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(Greeting, self).dispatch(*args, **kwargs)

    def post(self, request):
        resp = twilio.twiml.Response()
        resp.say("Let's set up your voicemail.  Leave your greeting and press star when you are done.")
        resp.record(method="GET",maxLength="20", finishOnKey="*", action="/calls/greeting")
        resp.say("Thanks")
        return HttpResponse(resp, content_type='application/xml')

    def get(self, request):
        resp = twilio.twiml.Response()
        print request.GET
        print request.POST
        resp.say("Thank you!")
        return HttpResponse(resp, content_type='application/xml')


class LeaveAMessage(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(Greeting, self).dispatch(*args, **kwargs)

    def post(self, request):
        resp = twilio.twiml.Response()
        resp.play(url='http://api.twilio.com/2010-04-01/Accounts/AC1df99c5915638a2c18f2e0a700de59cb/Recordings/REfe2d45c5a8aa90ec23b6b5303c5dd85a')
        resp.record(method="GET",maxLength="20", finishOnKey="*", action="/calls/message")
        resp.say("Thanks")
        return HttpResponse(resp, content_type='application/xml')

    def get(self, request):
        resp = twilio.twiml.Response()
        resp.say("Message has been saved!")
        return HttpResponse(resp, content_type='application/xml')
