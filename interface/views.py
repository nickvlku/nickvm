from django.shortcuts import render, render_to_response

# Create your views here.
from django.template.context import RequestContext


def setup_vm(request):
    return render_to_response("setup_vm.html", context_instance=RequestContext(request))