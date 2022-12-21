from django.db import models

from datetime import datetime
from django.urls import reverse
from django.utils.text import slugify

from tinymce import models as tinymce_models

class Restaurant(models.Model):
    NUMBER_OF_STARS_CHOICES = [
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]

    slug = models.SlugField(blank=True, null=True)
    title = models.CharField(max_length=200)
    thumb_nail = models.ImageField(upload_to="photos/%Y/%m/%d/")
    owner_description = tinymce_models.HTMLField(null=True, blank=True, verbose_name="Owner's Description")
    stars = models.IntegerField(
        choices=NUMBER_OF_STARS_CHOICES, 
        default=0, 
        verbose_name="Star Rating",
        help_text="Select the number of stars for this restaurant if any"
    )

    food_sold = models.CharField(max_length=200, blank=True, null=True, help_text="Enter coma separated main types of food sold by restaurant")
    website = models.URLField(max_length=200, blank=True, null=True)
    contact_number = models.CharField(null=True, blank=True, max_length=15)

    address_street = models.CharField(blank=True, null=True, max_length=100) 
    address_town = models.CharField(blank=True, null=True, max_length=100)
    address_postal_code = models.IntegerField(blank=True, null=True)

    business_times = models.CharField(
        blank=True, 
        null=True, 
        max_length=150,
        help_text="For example: Tuesday to Sunday, 10:00 to 22:00 OR Weekdays 10:00 to 21:00",
    )

    # I need to add the time the restaurant opens and closes

    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    is_published = models.BooleanField(default=True)

    date_added = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("dining_single_page", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title[:99], allow_unicode=True) #make a slug of no more than 100 characters
        super().save(*args, **kwargs)