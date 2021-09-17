# Generated by Django 3.2.4 on 2021-09-10 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_auto_20210813_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='academic_year',
            field=models.BigIntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='admission_date',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='city',
            field=models.CharField(default=None, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(default=None, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='guardian_contact',
            field=models.CharField(default=None, max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='medical_record',
            field=models.FileField(default=None, null=True, upload_to='files/'),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone_number',
            field=models.CharField(default=None, max_length=14, null=True),
        ),
    ]