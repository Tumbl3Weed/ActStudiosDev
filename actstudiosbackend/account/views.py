from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, authenticate
from django.apps import apps
from django.views.decorators.csrf import csrf_exempt
from account.models import Account
from account.serializers import ModelSerializer
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
        Model = Account.objects.all()

        serializer = ModelSerializer(
            Model)

        return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.error_messages, status=400)
