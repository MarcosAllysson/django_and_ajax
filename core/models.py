from django.db import models


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    bio = models.TextField()

    def __str__(self):
        return self.name
