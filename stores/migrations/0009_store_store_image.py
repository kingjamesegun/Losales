# Generated by Django 3.1.4 on 2021-06-15 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0008_store_s_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='store_image',
            field=models.ImageField(blank=True, null=True, upload_to='store_image'),
        ),
    ]
