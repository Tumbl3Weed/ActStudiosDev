# Generated by Django 4.0.3 on 2022-03-11 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_remove_student_teachers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(blank=True, to='account.teacher'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='schoolsTeachingAt',
            field=models.ManyToManyField(blank=True, to='account.school'),
        ),
    ]