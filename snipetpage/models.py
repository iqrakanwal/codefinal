from django.db import models

# Create your models here.


class snips(models.Model):
   snip_name= models.CharField(max_length=200)
