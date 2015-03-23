import random
from swampdragon import route_handler
from swampdragon.pubsub_providers.data_publisher import publish_data
from swampdragon.route_handler import BaseRouter
from tornado.ioloop import PeriodicCallback

pcb = None

class CallStatusRouter(BaseRouter):
    route_name = 'calls'

    def get_subscription_channels(self, **kwargs):
        broadcast_call_status()
        return ['call_status']


def broadcast_call_status():
    print "IN HEREtoo"

    global pcb
    if pcb is None:
        pcb = PeriodicCallback(broadcast_call_status, 500)
        pcb.start()

    print "HELLO"
    publish_data('call_status', {
        'status': random.randint(0, 1000)
    })


route_handler.register(CallStatusRouter)