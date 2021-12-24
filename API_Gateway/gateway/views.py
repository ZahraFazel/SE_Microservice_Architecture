from django.http import JsonResponse
import requests
from rest_framework.status import *
from API_Gateway.settings import ADMIN_URL, DOCTOR_URL, PATIENT_URL, PRESCRIPTION_URL, DB_AGGREGATOR_URL
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from django.utils.timezone import datetime


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


@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def signup_patient(request):
    name = request.POST['name']
    national_code = request.POST['national_code']
    password = request.POST['password']
    params = {'name': name, 'national_code': national_code, 'password': password}
    res = requests.post(PATIENT_URL + 'patient/signup_patient/', data=params)
    if res.status_code == HTTP_201_CREATED:
        return JsonResponse(res.json(), status=HTTP_200_OK)
    return JsonResponse(res.json(), status=HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def login_patient(request):
    name = request.POST['name']
    national_code = request.POST['national_code']
    password = request.POST['password']
    params = {'name': name, 'national_code': national_code, 'password': password}
    res = requests.post(PATIENT_URL + 'patient/login_patient/', data=params)
    if res.status_code == HTTP_200_OK:
        return JsonResponse(res.json(), status=HTTP_200_OK)
    return JsonResponse(res.json(), status=HTTP_401_UNAUTHORIZED)


@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def prescript(request):
    try:
        token = request.META.get('HTTP_AUTHORIZATION').split(' ')[-1]

        doctor_val_res = requests.post(DOCTOR_URL + 'doctor/validate_with_token/', data={'token': token})
        if doctor_val_res.status_code != HTTP_200_OK:
            return JsonResponse({'error': 'Not a doctor!'}, status=HTTP_401_UNAUTHORIZED)
        patient_national_code = request.POST['patient_national_code']
        patient_val_res = requests.post(PATIENT_URL + 'patient/validate_with_national_code/', data={'national_code': patient_national_code})
        if patient_val_res.status_code != HTTP_200_OK:
            return JsonResponse({'error': 'There is no patient with this national code!'}, status=HTTP_404_NOT_FOUND)
        params = {'doctor_id': doctor_val_res.json()['id'], 'patient_id': patient_val_res.json()['id'],
                    'drugs': request.POST['drugs'], 'date': request.POST.get('date', '0000-01-01')}
        prescript_res = requests.post(PRESCRIPTION_URL + 'prescription/new_prescription/', data=params)
        if prescript_res.status_code == HTTP_200_OK:
            return JsonResponse(prescript_res.json(), status=HTTP_201_CREATED)
        
        return JsonResponse(prescript_res.json(), status=HTTP_500_INTERNAL_SERVER_ERROR)

        
    except:
        return JsonResponse({'error': 'Not a doctor wtffffff'}, status=HTTP_401_UNAUTHORIZED)


@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def list_patient_prescriptions(request):
    try:
        token = request.META.get('HTTP_AUTHORIZATION').split(' ')[-1]
        patient_val_res = requests.post(PATIENT_URL + 'patient/validate_with_token/', data={'token': token})
        if patient_val_res.status_code != HTTP_200_OK:
            return JsonResponse({'error': 'Not a patient!'}, status=HTTP_401_UNAUTHORIZED)
        patient_id = patient_val_res.json()['id']
        prescription_list_res = requests.post(DB_AGGREGATOR_URL + 'list_patient_prescriptions/', {'id': patient_id})
        if prescription_list_res.status_code == HTTP_200_OK:
            return JsonResponse(prescription_list_res.json(), status=HTTP_200_OK)
        return JsonResponse(prescription_list_res.json(), status=HTTP_500_INTERNAL_SERVER_ERROR)
    except:
        return JsonResponse({'error': 'Not a patient'}, status=HTTP_401_UNAUTHORIZED)


@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def list_doctor_prescriptions(request):
    try:
        token = request.META.get('HTTP_AUTHORIZATION').split(' ')[-1]
        doctor_val_res = requests.post(DOCTOR_URL + 'doctor/validate_with_token/', data={'token': token})
        if doctor_val_res.status_code != HTTP_200_OK:
            return JsonResponse({'error': 'Not a doctor!111'}, status=HTTP_401_UNAUTHORIZED)
        doctor_id = doctor_val_res.json()['id']
        prescription_list_res = requests.post(DB_AGGREGATOR_URL + 'list_doctor_prescriptions/', {'id': doctor_id})
        print("!!!!!!!!!!!!!! ", prescription_list_res)
        if prescription_list_res.status_code == HTTP_200_OK:
            return JsonResponse(prescription_list_res.json(), status=HTTP_200_OK)
        return JsonResponse(prescription_list_res.json(), status=HTTP_500_INTERNAL_SERVER_ERROR)
    except:
        return JsonResponse({'error': 'Not a doctor!22222'}, status=HTTP_401_UNAUTHORIZED)

