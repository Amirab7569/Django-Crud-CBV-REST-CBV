from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_snippet(self):
        return self.body[0:5]
    
    def get_absolute_api_url(self):
        return reverse("home:api-v1:post-detail", kwargs={"pk": self.pk})
    
    
    class Meta:
        ordering = ['-created']