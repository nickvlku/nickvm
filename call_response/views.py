from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

import twilio.twiml


@csrf_exempt
def index(request):
    resp = twilio.twiml.Response()
    resp.say("Hello Monkey")

    return HttpResponse(resp, content_type='application/xml')


class Greeting(View):
    def get(self, request):
        resp = twilio.twiml.Response()
        resp.say("Let's set up your voicemail.  Leave your greeting and press star when you are done.")
        resp.record(method="GET",maxlength="20",finishonkey="*", action="/save")
        resp.say("Thanks")
        return HttpResponse(resp, content_type='application/xml')

    def post(self, request):
        resp = twilio.twiml.Response()
        resp.say("Thank you!")
        return HttpResponse(resp, content_type='application/xml')
