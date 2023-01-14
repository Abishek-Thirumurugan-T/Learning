from django.db import models


class Veggie(models.Model):
  category= models.CharField(max_length=2000)
  price= models.IntegerField(max_length=11)
  image=models.CharField(max_length=10000)
  name= models.CharField(max_length=2000)
  class Meta:
        db_table = 'veggie'#to override defaullt table name - appname_modelclassname