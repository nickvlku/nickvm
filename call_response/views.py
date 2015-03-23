import json

from django.http.response import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from twilio.rest.exceptions import TwilioRestException

import twilio.twiml
from interface.models import PhoneNumber, Call, Greeting as GreetingModel
from nickvm.twilio_client import configured_twilio_client
from nickvm.utils import convert_to_e164


def JSONResponse(response, **kwargs):
    j = json.dumps(response)
    return HttpResponse(j, content_type="application/json", **kwargs)


class CallAction(View):

    def post(self, request):
        to_number = request.POST.get('to_number', None)
        if to_number is None:
            return JSONResponse({"status": "error", "error": "to_number not specified"}, status=400)
        to_number = convert_to_e164(to_number)

        try:
            call = configured_twilio_client.calls.create(to=to_number,
                                                         from_="+14152344066",
                                                         url="https://xkifnqedgw.localtunnel.me/api/greeting")
            return JSONResponse({"status": "executed", "sid": call.sid})
        except TwilioRestException as te:
            print te
            return JSONResponse({"error": "could not make call"}, status=404)


class Greeting(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(Greeting, self).dispatch(*args, **kwargs)

    def post(self, request):
        resp = twilio.twiml.Response()
        resp.say("Let's set up your voicemail.  Leave your greeting and press star when you are done.")
        resp.record(method="GET",maxLength="20", finishOnKey="*", action="https://xkifnqedgw.localtunnel.me/api/greeting")
        resp.say("Thanks")
        return HttpResponse(resp, content_type='application/xml')

    def get(self, request):
        resp = twilio.twiml.Response()
        print request.GET
        print request.POST

        c = Call()
        c.sid = request.GET.get("CallSid")
        c.status = 'completed'
        c.to_number = request.GET.get('Called', None)
        c.from_number = request.GET.get('From', None)
        c.save()

        GreetingModel.objects.all().update(active=False)

        g = GreetingModel()
        g.phone_number = PhoneNumber.objects.first()
        g.active = True
        g.audio_file_link = request.GET.get('RecordingUrl')
        g.originating_call = c
        g.save()
        resp.say("Thank you!")
        return HttpResponse(resp, content_type='application/xml')


class LeaveAMessage(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(LeaveAMessage, self).dispatch(*args, **kwargs)

    def post(self, request):
        resp = twilio.twiml.Response()
        resp.play(url='http://api.twilio.com/2010-04-01/Accounts/AC1df99c5915638a2c18f2e0a700de59cb/Recordings/REfe2d45c5a8aa90ec23b6b5303c5dd85a')
        resp.record(method="GET",maxLength="20", finishOnKey="*", action="/api/message")
        resp.say("Thanks")
        return HttpResponse(resp, content_type='application/xml')

    def get(self, request):
        resp = twilio.twiml.Response()
        resp.say("Message has been saved!")
        return HttpResponse(resp, content_type='application/xml')


class CallStatus(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(CallStatus, self).dispatch(*args, **kwargs)

    def get(self, request, call_id):
        try:
            ci = configured_twilio_client.calls.get(call_id)
            return JSONResponse({
                "sid": call_id,
                "status": ci.status,
                "answered_by": ci.answered_by,
                "to_formatted": ci.to_formatted }, status=200)
        except TwilioRestException as te:
           return JSONResponse({"status": "error", "error": "could not find call with id %s" % call_id}, status=404)


class GreetingStatus(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(GreetingStatus, self).dispatch(*args, **kwargs)

    def get(self, request):
        g = GreetingModel.objects.filter(active=True)
        if len(g) > 0:
            return JSONResponse({"status": "created", "greeting_url": g[0].audio_file_link})
        else:
            return JSONResponse({"status": "not_created"})