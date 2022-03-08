from asyncio.windows_events import NULL
from contextlib import nullcontext
from os import access
from pyexpat import model
from turtle import onclick
from rest_framework import serializers
from account.models import Account
from django.apps import apps


class ModelSerializer (serializers.ModelSerializer):

    class Meta():
        model = Account
        # fields = '__all__'
        exclude = ['password']
        # model = apps.get_model(appName, modelName)
