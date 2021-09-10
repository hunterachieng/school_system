# Generated by Django 3.2.4 on 2021-09-10 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_alter_student_guardian_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='nationality',
            field=models.CharField(choices=[('K', 'Kenyan'), ('U', 'Ugandan'), ('R', 'Rwandan'), ('S', 'Sudan'), ('S', 'South Sudan')], default=None, max_length=10, null=True),
        ),
    ]
