# Generated by Django 5.0.1 on 2025-02-11 05:36

import ckeditor_uploader.fields
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Country')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentProcess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.CharField(max_length=255, verbose_name='ID of created payment')),
                ('payment_url', models.CharField(max_length=255, verbose_name='URL of created payment')),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Brand')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Description')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.country', verbose_name='Country')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='Image')),
                ('review', models.CharField(max_length=1000, verbose_name='Review')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date of creation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_ordered', models.BooleanField(default=False, verbose_name='Is ordered')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('payment_process', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order', to='core.paymentprocess', verbose_name='Payment')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=200, verbose_name='Model')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='Slug')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Description')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date of creation')),
                ('price', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Price, $')),
                ('is_available', models.BooleanField(default=True, verbose_name='Availability')),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity')),
                ('discount', models.IntegerField(default=0, verbose_name='Discount, %')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.brand', verbose_name='Brand')),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Quantity')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordered_products', to='core.order', verbose_name='Order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product', verbose_name='Product')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Review text')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date of creation')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='core.product', verbose_name='Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
