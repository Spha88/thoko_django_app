from datetime import datetime
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Activity(models.Model): 
    slug = models.SlugField(blank=True, null=True)
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=150)
    thumb_nail = models.ImageField(upload_to="photos/%Y/%m/%d/")
    excerpt = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    published = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now)

    class Meta: 
        verbose_name_plural = "Activities"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("single_activity_page", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title[:99], allow_unicode=True) #make a slug of no more than 100 characters
        super().save(*args, **kwargs)