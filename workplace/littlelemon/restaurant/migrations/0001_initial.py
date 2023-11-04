# Generated by Django 4.2.7 on 2023-11-04 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
                ('No_of_guests', models.IntegerField()),
                ('BokkingDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=255)),
                ('Price', models.FloatField()),
                ('Inventory', models.IntegerField()),
            ],
        ),
    ]