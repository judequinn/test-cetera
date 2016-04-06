from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Response(models.Model):
    full_name = models.CharField(max_length=255)
    text = models.TextField()
    email = models.EmailField()
    of_type = models.ManyToManyField(Type)


    def __str__(self):
        return self.full_name + ' (' + self.email + ')'

