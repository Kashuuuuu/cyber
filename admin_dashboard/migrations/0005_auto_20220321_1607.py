# Generated by Django 3.2.6 on 2022-03-21 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0004_alter_admin_profile_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='favicon',
            field=models.ImageField(upload_to='logo/'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='logo',
            field=models.ImageField(upload_to='logo/'),
        ),
    ]
