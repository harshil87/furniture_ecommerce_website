# Generated by Django 4.1.5 on 2023-04-04 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0013_alter_checkout_checkout_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='checkout_date',
        ),
    ]
