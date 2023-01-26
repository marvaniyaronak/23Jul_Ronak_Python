from django.db import models

# Create your models here.
class book_model(models.Model):
    tital=models.CharField(max_length=20)
    author=models.CharField(max_length=20)
    publisher=models.CharField(max_length=20)
    def __str__(self):
        return self.unm