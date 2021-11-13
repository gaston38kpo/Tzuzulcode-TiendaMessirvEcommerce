# Generated by Django 3.2.9 on 2021-11-13 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=1000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image_url', models.CharField(max_length=255)),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
