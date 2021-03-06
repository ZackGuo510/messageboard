from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=30)
    text = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:20] + '...'
