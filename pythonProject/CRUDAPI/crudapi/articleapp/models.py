from django.db import models

# Create your models here.

class ArticleInfo(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    comment = models.CharField(max_length=100)
    summary = models.CharField(max_length=100)

    def __str__(self):
        return self.title