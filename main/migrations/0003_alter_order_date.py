# Generated by Django 4.1.4 on 2022-12-11 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(verbose_name='m-d-Y'),
        ),
    ]