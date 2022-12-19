from django.contrib import admin

from .models import Restaurant

class RestaurantAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    list_display = ('title', 'stars', 'address_street', 'opening_day', 'closing_day')
    fieldsets = (
        (None, {
            'fields': ('slug', 'title', 'thumb_nail', 'owner_description', 'stars')
        }),
        ('Address', {
            'classes': ('collapse',),
            'fields': ('address_street', 'address_town', 'address_postal_code')
        }),
        ('Opening time', {
            'description': '<h3>Choose the opening and closing day of the week for this restaurant.</h3>',
            'classes': ('collapse',),
            'fields': ('opening_day', 'closing_day')
        }),
        ('Images', {
            'description': '<h3>Add 5 images to the restaurant page</h3>',
            'classes': ('collapse',),
            'fields': ('photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5')
        })
    )

admin.site.register(Restaurant, RestaurantAdmin)
