# Generated by Django 4.2.6 on 2024-01-07 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='price',
            field=models.PositiveIntegerField(default=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='credit',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='coach',
            name='price_per_segment',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='seatreservation',
            name='age',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='stop',
            name='order',
            field=models.IntegerField(null=True),
        ),
    ]