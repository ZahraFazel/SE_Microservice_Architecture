from django.shortcuts import render
from django.http import JsonResponse
import requests
from rest_framework.response import Response
from rest_framework.status import *
from API_Gateway.settings import ADMIN_URL
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer


@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def login_admin(request):
    username = request.POST['username']
    print('------------------ username: ' + username)
    password = request.POST['password']
    print('------------------ password: ' + password)
    params = {'username': username, 'password': password}
    res = requests.post(ADMIN_URL + 'system_admin/login_admin/', data=params)
    print('------------------ content', res.json())
    if res.status_code == 200:
        return JsonResponse(res.json(), status=HTTP_200_OK)
    return JsonResponse(res.json(), status=HTTP_401_UNAUTHORIZED)
