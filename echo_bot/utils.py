from viberbot import Api

from viberbot.api.bot_configuration import BotConfiguration

from django.conf import settings



bot_configuration = BotConfiguration(
    name = 'Сеансы',
    avatar = 'https://image.freepik.com/free-vector/_100823-20.jpg',
    auth_token = settings.VIBER_AUTH_TOKEN
)

viber = Api(bot_configuration)