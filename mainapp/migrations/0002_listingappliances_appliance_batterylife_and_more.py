# Generated by Django 4.1.7 on 2023-04-18 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listingappliances',
            name='appliance_batterylife',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='listingappliances',
            name='appliance_powerconsumptions',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='listingappliances',
            name='appliance_size',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='listingappliances',
            name='appliance_weight',
            field=models.IntegerField(default=0),
        ),
    ]
