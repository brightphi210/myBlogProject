from django.db import models
from django.contrib.auth.models import User

# Create your models here.

 

class Comment(models.Model):
    commentField = models.TextField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.commentField
    


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    dateTIme = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
   
