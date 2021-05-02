# Generated by Django 3.1.1 on 2021-04-19 17:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0006_auto_20210419_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerorders',
            name='discount',
            field=models.CharField(blank=True, max_length=3, null=True, validators=[django.core.validators.RegexValidator(regex='^[0-9]')]),
        ),
        migrations.AlterField(
            model_name='customerorders',
            name='final_price',
            field=models.CharField(blank=True, max_length=3, null=True, validators=[django.core.validators.RegexValidator(regex='^[0-9]')]),
        ),
        migrations.AlterField(
            model_name='customerorders',
            name='ordered_quantity',
            field=models.CharField(blank=True, max_length=3, null=True, validators=[django.core.validators.RegexValidator(regex='^[0-9]')]),
        ),
    ]