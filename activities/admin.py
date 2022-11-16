from django.contrib import admin
from .models import Activity

class ActivityAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)

admin.site.register(Activity, ActivityAdmin)

# Register your models here.
