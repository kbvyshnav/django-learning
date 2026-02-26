from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    age = models.IntegerField()

    def __str__(self):
        return self.name
