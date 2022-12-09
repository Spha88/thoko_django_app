from datetime import datetime
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from tinymce import models as tinymce_models

class Activity(models.Model): 
    slug = models.SlugField(blank=True, null=True)
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=150)
    thumb_nail = models.ImageField(upload_to="photos/%Y/%m/%d/")
    excerpt = tinymce_models.HTMLField(null=True, blank=True, help_text="Excerpt is made from the first paragraph of content")
    content = tinymce_models.HTMLField(null=True, blank=True)

    contact_person = models.CharField(null=True, blank=True, max_length=150)
    location = models.CharField(null=True, blank=True, max_length=150)
    website = models.URLField(db_index=True, null=True, blank=True, max_length=150)
    email = models.EmailField(null=True, blank=True, max_length=150)
    contact_number = models.CharField(null=True, blank=True, max_length=150)
    facebook_page_name = models.CharField(null=True, blank=True, max_length=150)
    facebook_page_link = models.URLField(db_index=True, null=True, blank=True, max_length=150)
    twitter_handle = models.CharField(null=True, blank=True, max_length=150)
    twitter_profile_link = models.URLField(db_index=True, null=True, blank=True, max_length=150)

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