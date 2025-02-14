from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.
class About(models.Model):
    # Basic information
    name = models.CharField(max_length=100)
    profile_picture = models.ImageField(default="portfolio\static\images\DSC_0032-removebg-preview (1).png",  upload_to='profile_pics')
    email = models.EmailField()
    
    # social links
    linkedin_url = models.URLField(max_length=500)
    instagram_url = models.URLField(max_length=500)
    x_url = models.URLField(max_length=500)
    facebook_url = models.URLField(max_length=500)


    def __str__(self):
        return self.name    
    

class Patents(models.Model):
    CATEGORY_CHOICES = [
        ('IU', 'Indian Utility'),
        ('ID', 'Indian Design'),
        ('FD', 'Foreign Design')
    ]
    
    title = models.CharField(max_length=600)
    granted_on = models.CharField(max_length=10)
    link = models.URLField(max_length=700)
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES)
    
 
    
    def __str__(self):
        return self.title
    
    

    
