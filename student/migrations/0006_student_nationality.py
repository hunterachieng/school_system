# Generated by Django 3.2.4 on 2021-07-30 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_alter_student_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='nationality',
            field=models.CharField(choices=[('K', 'Kenyan'), ('U', 'Ugandan'), ('R', 'Rwandan'), ('S', 'Sudan'), ('S', 'South Sudan')], default=None, max_length=10),
        ),
    ]
