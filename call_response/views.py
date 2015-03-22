from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import twilio.twiml


@csrf_exempt
def index(request):
    resp = twilio.twiml.Response()
    resp.say("Hello Monkey")

    return HttpResponse(resp, content_type='application/xml')