from django.db import models

# Create your models here.

class info(models.Model):
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=40)
    place = models.CharField(max_length=60)

    def __str__(self):
        return self.email
