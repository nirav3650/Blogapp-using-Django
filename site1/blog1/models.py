from django.db import models

# Create your models here.

class Blogpost(models.Model):
    blog_title = models.CharField(max_length=  200)
    blog_description = models.TextField(null=True)

    def __str__(self):
        return self.blog_title
