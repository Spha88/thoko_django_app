from datetime import datetime
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from tinymce import models as tinymce_models

class Attraction(models.Model): 
    NUMBER_OF_STARTS_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    slug = models.SlugField(blank=True, null=True)
    title = models.CharField(max_length=150)
    thumb_nail = models.ImageField(upload_to="photos/%Y/%m/%d/")
    description = tinymce_models.HTMLField(null=True, blank=True)

    stars = models.IntegerField(
        choices=NUMBER_OF_STARTS_CHOICES, 
        default=0, 
        verbose_name="Star rating",
        help_text="Select the number of start as per the Tourism Grading Council"
    )

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
        verbose_name_plural = "Attractions"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("single_attraction_page", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title[:99], allow_unicode=True) #make a slug of no more than 100 characters
        super().save(*args, **kwargs)
