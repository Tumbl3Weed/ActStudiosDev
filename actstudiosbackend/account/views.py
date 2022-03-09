from asyncio.windows_events import NULL
from gettext import NullTranslations
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, authenticate
from django.apps import apps
from django.views.decorators.csrf import csrf_exempt
from account import models
from account import serializers
from argparse import ArgumentParser
from rest_framework.parsers import JSONParser


def register_view(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse()


@csrf_exempt
def modelCRUD(request):

    wordPlay = request.path_info.split('/')
    while("" in wordPlay):
        wordPlay.remove("")

    print(request.body)
    if request.method == 'GET':
        if 'Account' in wordPlay:
            Model = models.Account.objects.all()
            serializer = serializers.AccountModelSerializer(Model, many=True)
            return JsonResponse(serializer.data, safe=False)
        if 'School' in wordPlay:
            Model = models.School.objects.all()
            serializer = serializers.SchoolModelSerializer(Model, many=True)
            return JsonResponse(serializer.data, safe=False)
        if 'Teacher' in wordPlay:
            Model = models.Teacher.objects.all()
            serializer = serializers.TeacherModelSerializer(Model, many=True)
            return JsonResponse(serializer.data, safe=False)
        if 'Student' in wordPlay:
            Model = models.Student.objects.all()
            serializer = serializers.StudentModelSerializer(Model, many=True)
            # print(serializer.data)
            return JsonResponse(serializer.data, safe=False)

        return JsonResponse(serializer.error_messages, status=400)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        if 'Account' in wordPlay:
            serializer = serializers.AccountModelSerializer(data=data)

        if 'School' in wordPlay:
            serializer = serializers.SchoolModelSerializer(data=data)

        if 'Teacher' in wordPlay:
            serializer = serializers.TeacherModelSerializer(data=data)

        if 'Student' in wordPlay:
            serializer = serializers.StudentModelSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.error_messages, status=400)

    elif request.method == 'DELETE':
        if 'Account' in wordPlay:
            Model = models.Account.objects.all()
            serializer = serializers.AccountModelSerializer(Model, many=True)
            print(serializer.data)
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.error_messages, status=400)


def modelCRUDpk(request, pk):

    wordPlay = request.path_info.split('/')
    while("" in wordPlay):
        wordPlay.remove("")

    print(wordPlay)
    if request.method == 'GET':
        if 'Account' in wordPlay:
            Model = models.Account.objects.get(pk=pk)
            serializer = serializers.AccountModelSerializer(Model)
            # print(serializer.data)
            return JsonResponse(serializer.data, safe=False)
        if 'School' in wordPlay:
            Model = models.School.objects.get(pk=pk)
            serializer = serializers.SchoolModelSerializer(Model)
            # print(serializer.data)
            return JsonResponse(serializer.data, safe=False)
        if 'Teacher' in wordPlay:
            Model = models.Teacher.objects.get(pk=pk)
            serializer = serializers.TeacherModelSerializer(Model)
            # print(serializer.data)
            return JsonResponse(serializer.data, safe=False)
        if 'Student' in wordPlay:
            Model = models.Student.objects.get(pk=pk)
            serializer = serializers.StudentModelSerializer(Model)
            # print(serializer.data)
            return JsonResponse(serializer.data, safe=False)

        return JsonResponse(serializer.error_messages, status=400)
