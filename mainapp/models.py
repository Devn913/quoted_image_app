from django.db import models

# Create your models here.


class contactMe(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=40)
    issue = models.TextField(max_length=2000)

    def __str__(self):
        return self.email