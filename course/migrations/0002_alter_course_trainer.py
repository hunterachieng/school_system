# Generated by Django 3.2.4 on 2021-08-13 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='trainer',
            field=models.CharField(max_length=20),
        ),
    ]
