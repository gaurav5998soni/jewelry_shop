# Generated by Django 2.2.11 on 2021-02-06 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jewelry', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='mobile',
            field=models.CharField(default=9090224699, max_length=12),
            preserve_default=False,
        ),
    ]