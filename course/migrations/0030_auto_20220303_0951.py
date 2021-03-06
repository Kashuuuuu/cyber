# Generated by Django 3.2.6 on 2022-03-03 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0011_auto_20220204_1106'),
        ('course', '0029_alter_course_detail_course_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_detail',
            name='course_instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_instructor_detail', to='user_profile.instructor'),
        ),
        migrations.AlterField(
            model_name='crs_review',
            name='crs',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course_review', to='course.course_detail'),
        ),
    ]
