# Generated by Django 3.2.7 on 2022-02-01 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0023_crs_review_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='crs_review',
            name='crs',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.course_detail'),
        ),
    ]
