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

    class Meta():
        model = models.School
        fields = '__all__'
        # exclude = ['password']
        # model = apps.get_model(appName, modelName)
