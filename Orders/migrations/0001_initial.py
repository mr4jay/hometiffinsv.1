# Generated by Django 3.1.1 on 2021-04-19 16:04

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerOrders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_date_time', models.DateTimeField(auto_now_add=True)),
                ('ordered_quantity', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.RegexValidator('^[6-9]\\d{9}$)', 'Only numbers')])),
                ('order_price', models.CharField(blank=True, max_length=3, null=True, validators=[django.core.validators.RegexValidator('^[6-9]\\d{9}$)', 'Only numbers')])),
                ('discount', models.CharField(blank=True, max_length=2, null=True, validators=[django.core.validators.RegexValidator('^[6-9]\\d{9}$)', 'Only numbers')])),
                ('final_price', models.CharField(blank=True, max_length=3, null=True, validators=[django.core.validators.RegexValidator('^[6-9]\\d{9}$)', 'Only numbers')])),
                ('is_delivered', models.BooleanField(default=False)),
                ('is_canceled', models.BooleanField(default=False)),
                ('reason_for_cancel', models.TextField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.foodproducts')),
            ],
        ),
    ]
