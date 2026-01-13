from django.db import models

# Create your models here.
class Chat(models.Model):

    name = models.CharField(max_length=255)
    message = models.CharField(max_length=500)
    createdAt = models.DateField(auto_now_add=True)