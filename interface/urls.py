from django.conf.urls import url, patterns

urlpatterns = patterns('',

    url(r'^setup_vm', 'interface.views.setup_vm')
)
