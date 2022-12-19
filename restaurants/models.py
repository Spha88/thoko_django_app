from django.db import models

from datetime import datetime
from django.urls import reverse
from django.utils.text import slugify

from tinymce import models as tinymce_models

class Restaurant(models.Model):
    NUMBER_OF_STARTS_CHOICES = [
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]

    DAYS_OF_WEEK_CHOICES = [
        ("MONDAY", "Monday"),
        ("TUESDAY", "Tuesday"),
        ("WEDNESDAY", "Wednesday"),
        ("THURSDAY", "Thursday"),
        ("FRIDAY", "Friday"),
        ("SATURDAY", "Saturday"),
        ("SUNDAY", "Sunday")
    ]

    slug = models.SlugField(blank=True, null=True)
    title = models.CharField(max_length=200)
    thumb_nail = models.ImageField(upload_to="photos/%Y/%m/%d/")
    owner_description = tinymce_models.HTMLField(null=True, blank=True, verbose_name="Owner's Description")
    stars = models.IntegerField(
        choices=NUMBER_OF_STARTS_CHOICES, 
        default=0, 
        verbose_name="Star Rating",
        help_text="Select the number of stars for this restaurant if any"
    )

    # need to install taggit and add a tags field

    address_street = models.CharField(blank=True, null=True, max_length=100)
    address_town = models.CharField(blank=True, null=True, max_length=100)
    address_postal_code = models.IntegerField(blank=True, null=True)

    contact_number = models.CharField(null=True, blank=True, max_length=15)

    opening_day = models.CharField(
        choices=DAYS_OF_WEEK_CHOICES,
        default="Monday",
        verbose_name="Opening day",
        help_text="Choose the day on which the restaurant opens for the week",
        max_length=20
    )
    closing_day = models.CharField(
        choices=DAYS_OF_WEEK_CHOICES,
        default="Sunday",
        verbose_name="Closing day",
        help_text="Choose the day on which the restaurant closes for the week",
        max_length=20
    )

    # I need to add the time the restaurant opens and closes

    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    is_published = models.BooleanField(default=True)

    date_added = models.DateTimeField(default=datetime.now, blank=True)

    



