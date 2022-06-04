from django.db import models

# Create your models here.

class Film(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    title = models.CharField(max_length=64, default = id)
    url = models.CharField(max_length=256, default="https://letterboxd.com/")

    def _str_(self):
        return self.id

class PrimaryUser(models.Model):
    username = models.CharField(max_length=15)

    def _str_(self):
        return self.username
