from django.urls import path

from . views import SetWebhookView,CallbackView,UnsetWebhook,TestView


urlpatterns = [
    path('set/', SetWebhookView.as_view()),
    path('callback/', CallbackView.as_view()),
    path('unset/', UnsetWebhook.as_view()),
    path('test/', TestView.as_view())
]
