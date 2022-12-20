from django.contrib import admin

from .models import Restaurant

class RestaurantAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    list_display = ('title', 'stars', 'address_street', 'contact_number')
    fieldsets = (
        (None, {
            'fields': ('slug', 'title', 'thumb_nail', 'owner_description', 'tags', 'stars', 'website', 'contact_number', 'business_times')
        }),
        ('Address', {
            'classes': ('collapse',),
            'fields': ('address_street', 'address_town', 'address_postal_code')
        }),
        ('Images', {
            'description': '<h3>Add 5 images to the restaurant page</h3>',
            'classes': ('collapse',),
            'fields': ('photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5')
        }),
        (None, {
            'fields': ('is_published', 'date_added')
        })
    )

admin.site.register(Restaurant, RestaurantAdmin)
