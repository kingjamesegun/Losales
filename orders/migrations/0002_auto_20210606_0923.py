# Generated by Django 3.1.4 on 2021-06-06 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='billing_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.billingaddress'),
        ),
    ]
