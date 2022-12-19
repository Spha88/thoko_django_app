from django.contrib import admin
from .models import Attraction

class AttractionAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)

admin.site.register(Attraction, AttractionAdmin)

