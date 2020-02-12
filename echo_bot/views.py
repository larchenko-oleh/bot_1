from django.views import View
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .utils import viber

from viberbot.api.viber_requests import ViberConversationStartedRequest
from viberbot.api.viber_requests import ViberFailedRequest
from viberbot.api.viber_requests import ViberMessageRequest
from viberbot.api.viber_requests import ViberSubscribedRequest
from viberbot.api.viber_requests import ViberUnsubscribedRequest
from viberbot.api.messages import TextMessage, PictureMessage

class SetWebhookView(View):
    def get(self, request):
        event_typpes=['subscribed','unsubscribed','conversation_started']
        viber.set_webhook(
            url='https://915222ea.ngrok.io/viber/callback/',
            webhook_events=event_typpes
        )
        return HttpResponse(status=200)


@method_decorator(csrf_exempt, name='dispatch')
class CallbackView(View):
    def post(self, request):
        viber_request = viber.parse_request(request.body)
        print(viber_request)
        if isinstance(viber_request,ViberMessageRequest):
            if isinstance(viber_request.message,TextMessage):
                viber.send_messages(viber_request.sender.id,TextMessage(text='Это текст'))
            elif isinstance(viber_request.message,PictureMessage):
                viber.send_messages(viber_request.sender.id,TextMessage(text='Это картинка'))
            elif isinstance(viber_request.message,TextMessage(text='Запорожье')):
                viber.send_messages(viber_request.sender.id,TextMessage(text='Это Город'))
        elif isinstance(viber_request, ViberConversationStartedRequest):
            if viber_request.context == "TEST":
                viber.send_messages(viber_request.user.id,TextMessage(text='ты выиграл 1000000'))
            elif viber_request.context == "Запорожье":
                viber.send_messages(viber_request.user.id,TextMessage(text='ты выиграл 5000000'))
        return HttpResponse(status=200)

class UnsetWebhook(View):
    def get(self, request):
        viber.unset_webhook()
        return HttpResponse(status=200)
        
class TestView(TemplateView):
    template_name = 'echo_bot/test.html'