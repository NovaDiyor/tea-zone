# Generated by Django 4.1.4 on 2022-12-15 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_client_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
