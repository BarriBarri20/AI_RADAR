# Generated by Django 3.0.5 on 2021-11-30 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20211130_0423'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScrapeHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]