from django.http import JsonResponse
import requests
from rest_framework.response import Response
from rest_framework.status import *
from API_Gateway.settings import ADMIN_URL, DOCTOR_URL
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer


@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def login_admin(request):
    username = request.POST['username']
    password = request.POST['password']
    params = {'username': username, 'password': password}
    res = requests.post(ADMIN_URL + 'system_admin/login_admin/', data=params)
    if res.status_code == HTTP_200_OK:
        return JsonResponse(res.json(), status=HTTP_200_OK)
    return JsonResponse(res.json(), status=HTTP_401_UNAUTHORIZED)


@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def signup_doctor(request):
    name = request.POST['name']
    national_code = request.POST['national_code']
    password = request.POST['password']
    params = {'name': name, 'national_code': national_code, 'password': password}
    res = requests.post(DOCTOR_URL + 'doctor/signup_doctor/', data=params)
    if res.status_code == HTTP_201_CREATED:
        return JsonResponse(res.json(), status=HTTP_200_OK)
    return JsonResponse(res.json(), status=HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def login_doctor(request):
    name = request.POST['name']
    national_code = request.POST['national_code']
    password = request.POST['password']
    params = {'name': name, 'national_code': national_code, 'password': password}
    res = requests.post(DOCTOR_URL + 'doctor/login_doctor/', data=params)
    if res.status_code == HTTP_200_OK:
        return JsonResponse(res.json(), status=HTTP_200_OK)
    return JsonResponse(res.json(), status=HTTP_401_UNAUTHORIZED)
