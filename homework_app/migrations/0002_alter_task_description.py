# Generated by Django 5.1.1 on 2024-10-03 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
