# Generated by Django 4.1.1 on 2022-10-12 18:23

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, max_length=70, unique=True)),
            ],
            options={
                'verbose_name': 'district',
                'verbose_name_plural': 'districts',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('title', models.CharField(max_length=230)),
                ('description', models.TextField()),
                ('no_of_floors', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(12)])),
                ('no_of_bathrooms', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(12)])),
                ('no_of_bedrooms', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(12)])),
                ('plot_area', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(50)])),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('has_watersupply', models.BooleanField(default=True)),
                ('has_electricity', models.BooleanField(default=True)),
                ('address_1', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=6)),
                ('is_occupied', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='properties.district')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'property',
                'verbose_name_plural': 'properties',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='PropertyImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='properties/')),
                ('property_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.property')),
            ],
            options={
                'verbose_name': 'propertyimage',
                'verbose_name_plural': 'Property Images',
            },
        ),
    ]
