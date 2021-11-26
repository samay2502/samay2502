from django.db import models

# Create your models here.
class raw(models.Model):
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=10)
    phone=models.PositiveIntegerField()
    mail=models.EmailField()
    def __str__(self):
        return self.username
    