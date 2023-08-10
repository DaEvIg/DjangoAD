# Generated by Django 4.2.3 on 2023-08-04 07:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0006_delete_mymodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='is_deleted',
        ),
        migrations.AlterField(
            model_name='ad',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
