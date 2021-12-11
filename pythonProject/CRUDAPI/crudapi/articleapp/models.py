from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ArticleInf(models.Model):
    articleid=models.IntegerField(primary_key=True)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    comment = models.CharField(max_length=100)
    summary = models.CharField(max_length=100)





#Crate/Insert/Add -POST
#Delete/Remve -Delete
#Retrive /Fetch - GET
#Update/Edit-PUT