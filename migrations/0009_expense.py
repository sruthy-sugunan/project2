# Generated by Django 3.2.7 on 2022-01-03 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0008_delete_expense'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense', models.CharField(max_length=100)),
                ('amount', models.FloatField()),
            ],
        ),
    ]
