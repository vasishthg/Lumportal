# Generated by Django 4.0.1 on 2022-01-17 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_oompa_name_oompa_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='oompa',
            name='name',
            field=models.CharField(default='eheh', max_length=200),
        ),
        migrations.AddField(
            model_name='oompa',
            name='passw',
            field=models.CharField(default='eheh', max_length=200),
        ),
    ]
