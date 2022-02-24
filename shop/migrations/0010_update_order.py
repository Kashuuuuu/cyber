# Generated by Django 3.2.6 on 2022-02-24 08:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0009_product_detail_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='update_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updt_id', models.CharField(blank=True, max_length=1000, null=True, unique=True, verbose_name='updt_pyment')),
                ('updt_date', models.DateTimeField(auto_now_add=True)),
                ('crs_orders', models.ManyToManyField(to='shop.courses_purchase_order')),
                ('prod_orders', models.ManyToManyField(to='shop.products_purchase_order')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
