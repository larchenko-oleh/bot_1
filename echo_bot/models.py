from django.db import models

'''class ViberUser(models.Model):
    viber_id=models.CharField(max_length=24)
    name=model.CharField(max_length=128)
    avatar=models.CharField()
    country=models.CharField(max_length=2)
    language=models.CharField(max_length=2)
    api_version=models.IntegerField()
    is_active=models.BooleanField()'''


class ViberUser(models.Model):
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    name = models.CharField(max_length=128)
    viber_id = models.CharField(max_length=24)
    country = models.CharField(max_length=2)
    is_active = models.BooleanField(null=True, blank=True)
    is_blocked = models.BooleanField(null=True, blank=True)
    api_version = models.PositiveSmallIntegerField()
    
    def __str__(self):
        return self.name

class Message(models.Model):
    text = models.TextField()
    timestamp = models.DateTimeField()
    user = models.ForeignKey("ViberUser", on_delete=models.SET_NULL, null=True)