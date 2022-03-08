from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, authenticate
from django.apps import apps
from django.views.decorators.csrf import csrf_exempt
from account import models
from account import serializers
from argparse import ArgumentParser


def register_view(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse()


@csrf_exempt
def modelCRUD(request):

    wordPlay = request.path_info.split('/')
    while("" in wordPlay):
        wordPlay.remove("")

    print(wordPlay)
    if request.method == 'GET':
        if 'Account' in wordPlay:
            Model = models.Account.objects.all()
            serializer = serializers.AccountModelSerializer(Model)
        if 'School' in wordPlay:
            Model = models.School.objects.all()
            serializer = serializers.SchoolModelSerializer(Model)

        return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.error_messages, status=400)
