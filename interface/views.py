from django.shortcuts import render, render_to_response

# Create your views here.
from django.template.context import RequestContext
from interface.models import PhoneNumber, Greeting


def setup_vm(request):
    ctx = {
        'greeting': Greeting.objects.get(active=True),
        'phone_numbers': PhoneNumber.objects.all()
    }
    return render_to_response("setup_vm.html", ctx, context_instance=RequestContext(request))