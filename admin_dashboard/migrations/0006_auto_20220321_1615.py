# Generated by Django 3.2.6 on 2022-03-21 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0005_auto_20220321_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='favicon',
            field=models.ImageField(blank=True, upload_to='logo/'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='logo',
            field=models.ImageField(blank=True, upload_to='logo/'),
        ),
    ]