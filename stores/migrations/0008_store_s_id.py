# Generated by Django 3.1.4 on 2021-06-03 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0007_store_subaccount_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='s_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
