from django.http.response import HttpResponse
from django.shortcuts import render

import twilio.twiml

def index(request):
    resp = twilio.twiml.Response()
    resp.say("Hello Monkey")

    return HttpResponse(resp, content_type='application/xml')