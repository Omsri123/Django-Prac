from django.db import models

# Create your models here.

class Blog(models.Model):
    blogTitle = models.CharField(max_length=20)
    blogBody = models.TextField()

    def __str__(self):
        return self.blogTitle
    
class comments(models.Model):
    blog = models.ForeignKey(Blog , on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()

    def __str__(self):
        return self.comment
