from django.db import models

class Alchol(models.Model):
     title = models.CharField(max_length = 200)
     body = models.TextField()
     writer = models.CharField(max_length = 200)

     def __str__(self):
         return self.title
     def summary(self):
        return self.body[:100]