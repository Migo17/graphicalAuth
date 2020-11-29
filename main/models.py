from django.db import models

# Create your models here.
class PhotoCrypto(models.Model):
    photo_name = models.CharField(max_length = 50, primary_key = True)
    photo_path = models.TextField()
    def __str__(self):
        return self.photo_name

class User(models.Model):
    username = models.CharField(max_length = 50)
    firstname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 50)
    photo_password = models.TextField()
    generated_id = models.TextField()

    def __str__(self):
        return self.username
