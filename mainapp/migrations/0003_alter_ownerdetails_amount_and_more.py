# Generated by Django 4.1.7 on 2023-04-18 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_listingappliances_appliance_batterylife_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownerdetails',
            name='Amount',
            field=models.IntegerField(default=50),
        ),
        migrations.AlterField(
            model_name='ownerdetails',
            name='Ownername',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='ownerdetails',
            name='Ownerstate',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='ownerdetails',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]
