from django.db import models

class project11(models.Model):
    name=models.CharField(max_length=10)
    price=models.PositiveIntegerField()
    des=models.TextField()
    def __str__(self):
        return self.name