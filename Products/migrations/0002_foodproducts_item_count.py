# Generated by Django 3.1.1 on 2021-04-24 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodproducts',
            name='item_count',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
