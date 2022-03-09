from asyncio.windows_events import NULL
from contextlib import nullcontext
from os import access
from pyexpat import model
from turtle import onclick
from rest_framework import serializers
from account import models
from django.apps import apps


class AccountModelSerializer (serializers.ModelSerializer):

    class Meta():
        model = models.Account
        # fields = '__all__'
        exclude = ['password']
        # model = apps.get_model(appName, modelName)


class SchoolModelSerializer (serializers.ModelSerializer):

    # teachersAtSchool = AccountModelSerializer(source='account_id')

    class Meta():
        model = models.School
        fields = '__all__'
        depth = 1


class StudentModelSerializer (serializers.ModelSerializer):

    class Meta():
        model = models.Student
        fields = '__all__'

        # exclude = ['password']
        # model = apps.get_model(appName, modelName)


class TeacherModelSerializer (serializers.ModelSerializer):
    # account = AccountModelSerializer(source='account_id')
    # schoolsTeachingAt = SchoolModelSerializer(many=True, read_only=True)
    # studentsTeaching = StudentModelSerializer(many=True, read_only=True)

    class Meta():
        model = models.Teacher
        fields = '__all__'
        depth = 1
