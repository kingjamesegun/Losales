# Generated by Django 3.1.4 on 2021-01-17 23:13

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
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True)),
                ('description', models.TextField()),
                ('country', models.CharField(max_length=200)),
                ('bank_code', models.IntegerField(null=True)),
                ('account_number', models.IntegerField(null=True)),
                ('slug', models.SlugField(unique=True)),
                ('twitter_handle', models.CharField(blank=True, max_length=100, null=True)),
                ('instagram_handle', models.CharField(blank=True, max_length=100, null=True)),
                ('store_subaccount_id', models.CharField(blank=True, max_length=200, null=True)),
                ('reference', models.CharField(blank=True, max_length=16, null=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('dispatch_rider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rider', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_product', models.CharField(max_length=200)),
                ('product_description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('shipping_fee', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.store')),
            ],
        ),
    ]
