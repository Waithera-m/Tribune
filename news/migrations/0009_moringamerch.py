# Generated by Django 3.0.6 on 2020-06-03 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20200527_1253'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoringaMerch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
    ]
