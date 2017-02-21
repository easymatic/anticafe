from channels.routing import route
from channels.staticfiles import StaticFilesConsumer

channel_routing = [
    route("websocket.receive", 'plan.consumers.ws_message'),
    route("http.request", StaticFilesConsumer()),
]
