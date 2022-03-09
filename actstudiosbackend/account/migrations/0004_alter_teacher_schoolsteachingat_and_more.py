# Generated by Django 4.0.3 on 2022-03-09 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_student_notes_alter_school_teachersatschool_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='schoolsTeachingAt',
            field=models.ManyToManyField(blank=True, to='account.school'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='studentsTeaching',
            field=models.ManyToManyField(blank=True, to='account.student'),
        ),
    ]
