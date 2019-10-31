# Generated by Django 2.2.6 on 2019-10-27 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0004_metadata_identifier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='metadata',
            name='id',
        ),
        migrations.AlterField(
            model_name='metadata',
            name='identifier',
            field=models.CharField(db_column='identifier', default='dft', max_length=100, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]