from django.db import models

# Create your models here.

class WaitList(models.Model):
    email = models.EmailField()
    create = models.DateTimeField(auto_now_add=True)
