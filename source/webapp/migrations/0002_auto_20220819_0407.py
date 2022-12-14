# Generated by Django 3.2.15 on 2022-08-18 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('phone', models.CharField(max_length=30, verbose_name='Phone')),
                ('address', models.CharField(max_length=30, verbose_name='Phone')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date creation')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Other', 'Разное'), ('IPad', 'IPad'), ('IPod', 'IPod'), ('IPhone', 'IPhone'), ('AirPods', 'AirPods'), ('MacOS', 'MacOS'), ('Apple Watch', 'Apple Watch')], default='Other', max_length=20, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_description',
            field=models.TextField(blank=True, max_length=2000, verbose_name='Product description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=100, verbose_name='Product name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='remainder',
            field=models.IntegerField(verbose_name='Remainder'),
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_products', to='webapp.order', verbose_name='Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_products', to='webapp.product', verbose_name='Product')),
            ],
        ),
        migrations.CreateModel(
            name='ItemInCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Quantity')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basket', to='webapp.product', verbose_name='Item in cart')),
            ],
        ),
    ]
