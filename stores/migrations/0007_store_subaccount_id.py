# Generated by Django 3.1.4 on 2021-06-03 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0006_auto_20210531_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='subaccount_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
