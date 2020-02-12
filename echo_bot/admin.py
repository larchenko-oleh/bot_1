# Register your models here.

from django.contrib import admin

from .models import ViberUser

from .models import Message

admin.site.register(ViberUser)

admin.site.register(Message)