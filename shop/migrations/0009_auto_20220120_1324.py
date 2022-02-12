# Generated by Django 3.2.7 on 2022-01-20 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_product_detail_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_detail',
            name='about_product',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='product_detail',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product_detail',
            name='product_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='product_detail',
            name='product_sku',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product_detail',
            name='product_tag',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product_detail',
            name='quntity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product_detail',
            name='slug',
            field=models.SlugField(max_length=1000, unique=True),
        ),
        migrations.AlterField(
            model_name='product_order',
            name='amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product_order',
            name='order_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product_order',
            name='payment',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product_order',
            name='quntity',
            field=models.IntegerField(),
        ),
    ]