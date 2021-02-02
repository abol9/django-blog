from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField(max_length=1000)
    body = models.TextField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    def __str__(self):
        return self.title + " ( {} ) ".format(self.created_date)
