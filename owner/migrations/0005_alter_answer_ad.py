# Generated by Django 3.2.9 on 2021-12-03 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0004_alter_answer_ad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='ad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='owner.advertisement'),
        ),
    ]
