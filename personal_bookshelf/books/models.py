from django.db import models


class author(models.Model):
    name = models.CharField(max_length=50,default="name")
    surname = models.CharField(max_length=100,default="surname")
    personal_troughts=models.TextField()

class book (models.Model):
    title= models.CharField(max_length=100,default="title")
    description= models.TextField()
    author = models.ForeignKey(author,on_delete=models.CASCADE)
    #author
    ganre = models.CharField(max_length=100,default="grene")
    release_date= models.DateTimeField()
    personal_trought= models.TextField()


