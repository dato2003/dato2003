from django.db import models

class user(models.Model):
    name = models.CharField(max_length=30)
    lasatname = models.CharField(max_length=50)
    email = models.EmailField()
    passsword = models.CharField(max_length=20)

