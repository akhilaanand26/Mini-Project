from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.urls import reverse
from users.models import User

# Create your models here.

class District(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=70, unique=True, blank=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'district'
        verbose_name_plural = 'districts'

    def __str__(self):
        return self.name

class Property(models.Model):
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    title = models.CharField(max_length=230)
    description = models.TextField()
    no_of_floors = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(12)])
    no_of_bathrooms = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(12)])
    no_of_bedrooms = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(12)])

    plot_area = models.PositiveIntegerField(validators=[MinValueValidator(50)]) # sqft
    
    price = models.DecimalField(max_digits=6, decimal_places=2)

    has_watersupply = models.BooleanField(default=True)
    has_electricity = models.BooleanField(default=True)

    address_1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    zip_code = models.CharField(max_length=6)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    is_occupied = models.BooleanField(default=False)

    created_at = models.DateTimeField(default=timezone.now) # can be edited/updated manually
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('properties:detail', args=[self.slug])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_at', )
        verbose_name = 'property'
        verbose_name_plural = 'properties'

class PropertyImages(models.Model):
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='properties/')

    def __str__(self):
        return self.property_id.title
    
    class Meta:
        verbose_name = 'propertyimage'
        verbose_name_plural = 'Property Images'