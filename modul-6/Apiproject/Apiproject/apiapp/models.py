from django.db import models

# Create your models here.

class user_info(models.Model):
    unm=models.CharField(max_length=20)
    sub=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    def __str__(self):
        return self.unm