# Generated by Django 3.2.9 on 2021-11-29 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0002_remove_advertisement_viewers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='media_file',
            field=models.FileField(upload_to='owner/'),
        ),
    ]