# Generated by Django 3.2.6 on 2022-03-06 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0030_auto_20220303_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_detail',
            name='student_no',
            field=models.IntegerField(default=0),
        ),
    ]
