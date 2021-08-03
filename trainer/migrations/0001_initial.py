# Generated by Django 3.2.4 on 2021-08-01 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=12)),
                ('last_name', models.CharField(max_length=20)),
                ('image', models.ImageField(default=None, upload_to='images/')),
                ('email', models.EmailField(default=None, max_length=254)),
                ('phone_number', models.CharField(default=None, max_length=14)),
                ('national_id', models.CharField(default=None, max_length=20)),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Others')], max_length=10)),
                ('city', models.CharField(max_length=10)),
                ('company', models.CharField(max_length=30)),
                ('course', models.CharField(max_length=20)),
                ('contract', models.FileField(upload_to='files/')),
                ('resume', models.FileField(upload_to='files/')),
                ('salary', models.BigIntegerField()),
            ],
        ),
    ]
