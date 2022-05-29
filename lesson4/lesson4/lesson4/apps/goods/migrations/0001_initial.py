# Generated by Django 4.0.4 on 2022-05-29 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('price', models.FloatField(default=0)),
                ('qty', models.TextField(blank=True, null=True)),
                ('distributor', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
