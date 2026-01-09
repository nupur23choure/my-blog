from django.db import models

# Create your models here.
class About(models.Model):
    about_heading = models.CharField(max_length=60)
    about_description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    class Meta:
        verbose_name_plural = "About"

    def __str__(self):
        return self.about_heading

class SocialMedia(models.Model):
    platform = models.CharField(max_length=60)
    link = models.URLField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.platform