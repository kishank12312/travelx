# Generated by Django 2.2.6 on 2019-11-21 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0012_auto_20191121_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passengers',
            name='email',
            field=models.EmailField(max_length=250, null=True, verbose_name='email'),
        ),
    ]
