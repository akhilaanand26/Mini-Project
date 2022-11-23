from django.contrib import admin
from .models import District, Property, PropertyImages

# Register your models here.

class PropertyImagesInline(admin.StackedInline):
    model = PropertyImages

class PropertyAdmin(admin.ModelAdmin):
    model = Property
    inlines = [PropertyImagesInline,]

    list_display = ('title', 'plot_area', 'price', 'zip_code', 'owner', 'is_occupied')

    fieldsets = (
        (None, { 'fields': ('title', 'description','owner', 'is_occupied',) }),
        ('Address', { 'fields': ('address_1', 'city', 'district', 'zip_code') }),
        ('Other Info', { 'fields': ('no_of_floors', 'no_of_bathrooms', 'no_of_bedrooms', 'plot_area', 'price', 'has_watersupply', 'has_electricity') }),
        ('Miscellaneous', { 'fields': ('created_at', 'slug') }),
    )

    search_fields = ('title', 'zip_code', 'city', 'description')

admin.site.register(Property, PropertyAdmin)
admin.site.register(PropertyImages)
admin.site.register(District)

