# Generated by Django 4.1.7 on 2023-03-29 10:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CheckOut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('checkout_email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('product_qty', models.FloatField()),
                ('products_id', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('Payment_status', models.TextField()),
                ('checkout_date', models.DateField(default=datetime.datetime(2023, 4, 28, 10, 50, 13, 847281, tzinfo=datetime.timezone.utc), verbose_name='expiration time (of ad)')),
            ],
        ),
    ]
