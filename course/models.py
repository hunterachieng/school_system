from django.db import models

# Create your models here.
class Course(models.Model):
    course_choice =((u'P',u'Python'),
    (u'J',u'JavaScript'),
    (u'K',u'Kotlin'),
    (u'U',u'UX Research'),
    (u'UI',u'UI/UX Design'),
    (u'P',u'Professional Development'),
    (u'N',u'Navigating Your Journey'))
    course_name = models.CharField(max_length=20,choices=course_choice)
    course_code_choice=((u'P',u'P-BackEnd'),
   ( u'J',u'J-FrontEnd'),
   (u'K',u'K-MobFront'),
   (u'U',u'U-Rsh'),
   (u'UI',u'UI/UX'),
   (u'p',u'PD'),
   (u'N',u'NYJ'))
    course_code = models.CharField(max_length=10,choices=course_code_choice)
    trainer = models.CharField(max_length=10)
    course_description = models.TextField()
    syllabus = models.FileField(upload_to='files/')
    


