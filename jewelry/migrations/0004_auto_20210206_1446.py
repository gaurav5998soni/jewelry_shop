# Generated by Django 2.2.11 on 2021-02-06 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jewelry', '0003_auto_20210206_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='lending_amount',
            field=models.CharField(default='0', max_length=40),
        ),
        migrations.AlterField(
            model_name='customer',
            name='total_intrest',
            field=models.CharField(default='0', max_length=40),
        ),
    ]
