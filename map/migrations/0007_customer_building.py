# Generated by Django 3.2.4 on 2021-06-28 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0006_customer_street'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='building',
            field=models.IntegerField(blank=True, null=True, verbose_name='Номер дома'),
        ),
    ]
