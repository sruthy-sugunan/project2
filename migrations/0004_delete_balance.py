# Generated by Django 3.2.7 on 2022-01-03 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0003_expense'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Balance',
        ),
    ]
