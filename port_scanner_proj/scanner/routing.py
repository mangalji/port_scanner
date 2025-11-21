from django.urls import path
from .consumers import PortScanConsumer

websocket_urlpatterns = [
    path("ws/scan/", PortScanConsumer.as_asgi()),
]
