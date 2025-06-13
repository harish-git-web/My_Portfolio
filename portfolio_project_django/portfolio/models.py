from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=30)
    description=models.TextField()
    link=models.URLField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return self.title
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"
