from django.db import models

# Create your models here.

class Section(models.Model):
    name = models.CharField(max_length=20,verbose_name="部门名")

    def __str__(self):
        return self.name

class Staff(models.Model):
    name = models.CharField(max_length=20,verbose_name="职工")
    salary = models.FloatField(verbose_name="工资")
    section = models.ForeignKey(Section,on_delete=models.CASCADE,verbose_name="部门",related_name='staffs')

    def __str__(self):
        return self.name
