# Generated by Django 4.0.3 on 2022-03-09 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_school_teachersatschool'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(blank=True, max_length=30, unique=True),
        ),
    ]
