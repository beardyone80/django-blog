from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.


class About(models.Model):
    """
    Stores a single about me text.
    """
    title = models.CharField(max_length=200, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class CollaborateRequest(models.Model):
    """
    Allows user to send collab request form
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"