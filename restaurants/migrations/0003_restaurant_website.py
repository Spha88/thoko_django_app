# Generated by Django 4.1.2 on 2022-12-20 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_restaurant_closing_day_alter_restaurant_opening_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]