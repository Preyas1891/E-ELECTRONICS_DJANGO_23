# Generated by Django 4.1.7 on 2023-04-18 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListingAppliances',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_id', models.CharField(blank=True, max_length=50, null=True)),
                ('view_count', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='images/')),
                ('video', models.FileField(blank=True, default='', null=True, upload_to='video/')),
                ('description', models.TextField(max_length=500)),
                ('country', models.CharField(max_length=50, verbose_name='Area')),
                ('appliance_type', models.CharField(max_length=50)),
                ('appliance_id', models.IntegerField(default=0)),
                ('OriginalCharger', models.BooleanField(default=False)),
                ('box', models.BooleanField(default=False)),
                ('OriginalBill', models.BooleanField(default=False)),
                ('warranty', models.BooleanField(default=False)),
                ('verified', models.BooleanField(default=False)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='OwnerDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ownername', models.CharField(max_length=30)),
                ('Owneremail', models.EmailField(max_length=254, unique=True)),
                ('Ownerphone', models.PositiveIntegerField()),
                ('Ownerstate', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=10)),
                ('Amount', models.IntegerField(default=1)),
                ('Approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='paymentdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderDate', models.DateTimeField(auto_created=True, auto_now=True)),
                ('user_id', models.CharField(default='', max_length=50)),
                ('owner_id', models.CharField(default='', max_length=50)),
                ('user', models.CharField(max_length=50)),
                ('Owner', models.CharField(max_length=50)),
                ('appliance_name', models.CharField(max_length=50)),
                ('PaymentVia', models.CharField(max_length=50)),
                ('PaymentMethod', models.CharField(max_length=50)),
                ('Amount', models.CharField(max_length=50)),
                ('transactionId', models.TextField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('mobile_num', models.IntegerField()),
                ('email_id', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('is_approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ProperFeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now=True)),
                ('rating', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1', max_length=20)),
                ('feedback', models.TextField()),
                ('feed_pos', models.FloatField(default=0.0)),
                ('feed_neg', models.FloatField(default=0.0)),
                ('Appliance_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.listingappliances')),
                ('cust_data', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.userregistration')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='file/')),
                ('booked', models.BooleanField(default=False)),
                ('date', models.DateField(null=True)),
                ('payment', models.BooleanField(default=False)),
                ('app_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.listingappliances')),
                ('owner_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.ownerdetails')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.userregistration')),
            ],
        ),
    ]