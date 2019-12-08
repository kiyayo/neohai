from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, UrlRouter
import chat.routing

application = ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(
        UrlRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})