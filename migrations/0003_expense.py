# Generated by Django 3.2.7 on 2022-01-03 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0002_delete_expense'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense', models.CharField(max_length=100)),
            ],
        ),
    ]