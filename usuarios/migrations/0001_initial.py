# Generated by Django 3.2.9 on 2021-11-13 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=50)),
            ],
        ),
    ]
