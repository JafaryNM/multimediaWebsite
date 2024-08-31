from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Slideshow(models.Model):
    title=models.TextField(max_length=300)
    image=models.ImageField(upload_to='slideshow')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    

class Service(models.Model):
    title=models.TextField(max_length=300)
    description=models.TextField()
    image=models.ImageField(upload_to='service')
    slug=models.SlugField(unique=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("service_detail", kwargs={"pk": self.pk})
    