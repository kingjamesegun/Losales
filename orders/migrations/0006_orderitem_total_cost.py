# Generated by Django 3.1.4 on 2021-06-07 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20210607_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='total_cost',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=12),
        ),
    ]
