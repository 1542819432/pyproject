from django.db import models

# Create your models here.

class Title(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Option(models.Model):
    choice = models.CharField(max_length=40)
    num = models.FloatField(default=0)
    title = models.ForeignKey(Title,on_delete=models.CASCADE,related_name='option')

    def __str__(self):
        return self.choice

