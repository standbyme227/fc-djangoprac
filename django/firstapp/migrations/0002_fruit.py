# Generated by Django 2.0.2 on 2018-02-06 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
    ]