# Generated by Django 4.1.2 on 2022-12-20 08:41

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('restaurants', '0004_remove_restaurant_closing_day_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='Add tags/comma separated names which related to the restaurant. e.g burgers, children, wifi, toys, pizza, breakfast ', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='business_times',
            field=models.CharField(blank=True, help_text='For example: Tuesday to Sunday, 10:00 to 22:00 OR Weekdays 10:00 to 21:00', max_length=150, null=True),
        ),
    ]
