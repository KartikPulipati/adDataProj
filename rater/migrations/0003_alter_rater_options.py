# Generated by Django 3.2.9 on 2021-12-17 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rater', '0002_alter_rater_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rater',
            options={'permissions': (('can_access_rater', 'Rater Permissions Kartik'),)},
        ),
    ]
