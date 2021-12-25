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
    res = requests.post(ADMIN_URL + 'system_admin/login/', data=params)
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
    res = requests.post(DOCTOR_URL + 'doctor/signup/', data=params)
    if res.status_code == HTTP_201_CREATED:
        return JsonResponse(res.json(), status=HTTP_201_CREATED)
    return JsonResponse(res.json(), status=HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def login_doctor(request):
    name = request.POST['name']
    national_code = request.POST['national_code']
    password = request.POST['password']
    params = {'name': name, 'national_code': national_code, 'password': password}
    res = requests.post(DOCTOR_URL + 'doctor/login/', data=params)
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
    res = requests.post(PATIENT_URL + 'patient/signup/', data=params)
    if res.status_code == HTTP_201_CREATED:
        return JsonResponse(res.json(), status=HTTP_201_CREATED)
    return JsonResponse(res.json(), status=HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def login_patient(request):
    name = request.POST['name']
    national_code = request.POST['national_code']
    password = request.POST['password']
    params = {'name': name, 'national_code': national_code, 'password': password}
    res = requests.post(PATIENT_URL + 'patient/login/', data=params)
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
        patient_val_res = requests.post(PATIENT_URL + 'patient/validate_with_national_code/',
                                        data={'national_code': patient_national_code})
        if patient_val_res.status_code != HTTP_200_OK:
            return JsonResponse({'error': 'There is no patient with this national code!'}, status=HTTP_404_NOT_FOUND)
        params = {'doctor_id': doctor_val_res.json()['id'], 'patient_id': patient_val_res.json()['id'],
                  'drugs': request.POST['drugs'], 'date': request.POST.get('date', datetime.now().strftime('%Y-%m-%d'))}
        prescript_res = requests.post(PRESCRIPTION_URL + 'prescription/new_prescription/', data=params)
        if prescript_res.status_code == HTTP_200_OK:
            return JsonResponse(prescript_res.json(), status=HTTP_201_CREATED)
        return JsonResponse(prescript_res.json(), status=HTTP_500_INTERNAL_SERVER_ERROR)
    except:
        return JsonResponse({'error': 'Not a doctor!'}, status=HTTP_401_UNAUTHORIZED)


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
            return JsonResponse({'error': 'Not a doctor!'}, status=HTTP_401_UNAUTHORIZED)
        doctor_id = doctor_val_res.json()['id']
        prescription_list_res = requests.post(DB_AGGREGATOR_URL + 'list_doctor_prescriptions/', {'id': doctor_id})
        if prescription_list_res.status_code == HTTP_200_OK:
            return JsonResponse(prescription_list_res.json(), status=HTTP_200_OK)
        return JsonResponse(prescription_list_res.json(), status=HTTP_500_INTERNAL_SERVER_ERROR)
    except:
        return JsonResponse({'error': 'Not a doctor!'}, status=HTTP_401_UNAUTHORIZED)


@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def list_prescriptions(request):
    try:
        token = request.META.get('HTTP_AUTHORIZATION').split(' ')[-1]
        admin_val_res = requests.post(ADMIN_URL + 'system_admin/validate_with_token/', data={'token': token})
        if admin_val_res.status_code != HTTP_200_OK:
            return JsonResponse({'error': 'Not an admin!'}, status=HTTP_401_UNAUTHORIZED)
        prescription_list_res = requests.post(DB_AGGREGATOR_URL + 'list_prescriptions/')
        if prescription_list_res.status_code == HTTP_200_OK:
            return JsonResponse(prescription_list_res.json(), status=HTTP_200_OK)
        return JsonResponse(prescription_list_res.json(), status=HTTP_500_INTERNAL_SERVER_ERROR)
    except:
        return JsonResponse({'error': 'Not an admin!'}, status=HTTP_401_UNAUTHORIZED)


@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def list_doctors(request):
    try:
        token = request.META.get('HTTP_AUTHORIZATION').split(' ')[-1]
        admin_val_res = requests.post(ADMIN_URL + 'system_admin/validate_with_token/', data={'token': token})
        if admin_val_res.status_code != HTTP_200_OK:
            return JsonResponse({'error': 'Not an admin!'}, status=HTTP_401_UNAUTHORIZED)
        doctor_list_res = requests.post(DB_AGGREGATOR_URL + 'list_doctors/')
        if doctor_list_res.status_code == HTTP_200_OK:
            return JsonResponse(doctor_list_res.json(), status=HTTP_200_OK)
        return JsonResponse(doctor_list_res.json(), status=HTTP_500_INTERNAL_SERVER_ERROR)
    except:
        return JsonResponse({'error': 'Not an admin!'}, status=HTTP_401_UNAUTHORIZED)


@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def list_patients(request):
    try:
        token = request.META.get('HTTP_AUTHORIZATION').split(' ')[-1]
        admin_val_res = requests.post(ADMIN_URL + 'system_admin/validate_with_token/', data={'token': token})
        if admin_val_res.status_code != HTTP_200_OK:
            return JsonResponse({'error': 'Not an admin!'}, status=HTTP_401_UNAUTHORIZED)
        patient_list_res = requests.post(DB_AGGREGATOR_URL + 'list_patients/')
        if patient_list_res.status_code == HTTP_200_OK:
            return JsonResponse(patient_list_res.json(), status=HTTP_200_OK)
        return JsonResponse(patient_list_res.json(), status=HTTP_500_INTERNAL_SERVER_ERROR)
    except:
        return JsonResponse({'error': 'Not an admin!'}, status=HTTP_401_UNAUTHORIZED)


@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def get_daily_statistics(request):
    try:
        token = request.META.get('HTTP_AUTHORIZATION').split(' ')[-1]
        admin_val_res = requests.post(ADMIN_URL + 'system_admin/validate_with_token/', data={'token': token})
        if admin_val_res.status_code != HTTP_200_OK:
            return JsonResponse({'error': 'Not an admin!'}, status=HTTP_401_UNAUTHORIZED)
        daily_statistics_res = requests.post(DB_AGGREGATOR_URL + 'get_daily_statistics/')
        if daily_statistics_res.status_code == HTTP_200_OK:
            return JsonResponse(daily_statistics_res.json(), status=HTTP_200_OK)
        return JsonResponse(daily_statistics_res.json(), status=HTTP_500_INTERNAL_SERVER_ERROR)
    except:
        return JsonResponse({'error': 'Not an admin!'}, status=HTTP_401_UNAUTHORIZED)


@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def get_admin_profile(request):
    try:
        token = request.META.get('HTTP_AUTHORIZATION').split(' ')[-1]
        admin_profile_res = requests.post(ADMIN_URL + 'system_admin/profile/', data={'token': token})
        if admin_profile_res.status_code != HTTP_200_OK:
            return JsonResponse({'error': 'Not an admin!'}, status=HTTP_401_UNAUTHORIZED)
        return JsonResponse(admin_profile_res.json(), status=HTTP_200_OK)
    except:
        return JsonResponse({'error': 'Not an admin!'}, status=HTTP_401_UNAUTHORIZED)


@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def get_doctor_profile(request):
    try:
        token = request.META.get('HTTP_AUTHORIZATION').split(' ')[-1]
        doctor_profile_res = requests.post(DOCTOR_URL + 'doctor/profile/', data={'token': token})
        if doctor_profile_res.status_code != HTTP_200_OK:
            return JsonResponse({'error': 'Not an doctor!'}, status=HTTP_401_UNAUTHORIZED)
        return JsonResponse(doctor_profile_res.json(), status=HTTP_200_OK)
    except:
        return JsonResponse({'error': 'Not an doctor!'}, status=HTTP_401_UNAUTHORIZED)


@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def get_patient_profile(request):
    try:
        token = request.META.get('HTTP_AUTHORIZATION').split(' ')[-1]
        patient_profile_res = requests.post(PATIENT_URL + 'patient/profile/', data={'token': token})
        if patient_profile_res.status_code != HTTP_200_OK:
            return JsonResponse({'error': 'Not an patient!'}, status=HTTP_401_UNAUTHORIZED)
        return JsonResponse(patient_profile_res.json(), status=HTTP_200_OK)
    except:
        return JsonResponse({'error': 'Not an patient!'}, status=HTTP_401_UNAUTHORIZED)
