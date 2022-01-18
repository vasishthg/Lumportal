# Generated by Django 4.0.1 on 2022-01-18 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_oompa_salary'),
        ('dashboard', '0008_alter_training_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='oompa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.oompa'),
        ),
    ]
