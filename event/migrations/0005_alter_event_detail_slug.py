# Generated by Django 3.2.7 on 2022-01-15 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_event_detail_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_detail',
            name='slug',
            field=models.SlugField(max_length=1000, null=True),
        ),
    ]