# Generated by Django 3.1.5 on 2021-02-15 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangogramm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.IntegerField(editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]