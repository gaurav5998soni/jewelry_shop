# Generated by Django 2.2.11 on 2021-02-06 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jewelry', '0002_customer_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='items',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='customer',
            name='lending_amount',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='customer',
            name='total_intrest',
            field=models.FloatField(default=0),
        ),
    ]