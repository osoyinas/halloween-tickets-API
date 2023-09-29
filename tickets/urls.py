from django.urls import path
from .views import CreateTicketAPIView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
urlpatterns = [
    path('tickets/',  csrf_exempt(CreateTicketAPIView.as_view()), name='ticket-list-create'),
]