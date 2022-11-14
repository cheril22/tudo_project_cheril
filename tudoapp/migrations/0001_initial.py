# Generated by Django 4.1.3 on 2022-11-14 13:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1024, null=True)),
                ('todays_price', models.FloatField(null=True)),
                ('offer_price', models.FloatField(null=True)),
                ('measuring_unit', models.CharField(default='Kg(s)', max_length=100)),
                ('available_quantity', models.FloatField(null=True)),
                ('min_available_qty', models.FloatField(default=1.0)),
                ('max_available_qty', models.FloatField(default=models.FloatField(null=True), null=True)),
                ('max_qty_allowed_per_order', models.FloatField(null=True)),
                ('gst', models.FloatField(default=0)),
                ('isActive', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Retailer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(blank=True, max_length=50)),
                ('lastName', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=25, null=True)),
                ('country', models.CharField(blank=True, max_length=25, null=True)),
                ('pin', models.CharField(blank=True, max_length=10, null=True)),
                ('icon', models.URLField(blank=True, max_length=1028, null=True)),
                ('emailId', models.EmailField(blank=True, max_length=254, unique=True)),
                ('primaryContactNumber', models.CharField(blank=True, max_length=15, null=True)),
                ('isMailVerified', models.BooleanField(default=False)),
                ('isPhoneVerified', models.BooleanField(default=False)),
                ('emailKey', models.CharField(blank=True, max_length=255, null=True)),
                ('password', models.CharField(max_length=50)),
                ('otp', models.CharField(blank=True, max_length=10, null=True)),
                ('otpGenTime', models.DateTimeField(auto_now=True)),
                ('isActive', models.BooleanField(default=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('djangoUser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='django_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isActive', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('commodity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commodity_for_order', to='tudoapp.commodity')),
                ('retailer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='retailer_for_order', to='tudoapp.retailer')),
            ],
        ),
        migrations.AddField(
            model_name='commodity',
            name='retailer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='retailer_for_commodity', to='tudoapp.retailer'),
        ),
    ]
