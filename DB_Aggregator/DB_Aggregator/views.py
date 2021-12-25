import requests
from django.http import JsonResponse
from rest_framework.decorators import renderer_classes, api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.status import HTTP_200_OK
from DB_Aggregator.settings import PATIENT_URL, DOCTOR_URL, PRESCRIPTION_URL


@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def list_patient_prescriptions(request):
    patient_id = request.POST['id']
    prescriptions_list_res = requests.post(PRESCRIPTION_URL + 'prescription/get_patient_prescriptions/', {'id': patient_id})
    prescriptions_list = prescriptions_list_res.json()['prescriptions']
    list_of_doctors_ids = [str(prescription[0]) for prescription in prescriptions_list]
    doctors_res = requests.post(DOCTOR_URL + 'doctor/get_doctors/', {'ids': ",".join(list_of_doctors_ids)})
    doctors = {}
    for doctor in doctors_res.json()['doctors']:
        doctors[doctor[0]] = doctor[1]
    output = []
    for prescription in prescriptions_list:
        output.append({'doctor_name': doctors[prescription[0]],
                       'drugs': prescription[1],
                       'date': prescription[2]})
    return JsonResponse({'list': output}, status=HTTP_200_OK, safe=False)


@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def list_doctor_prescriptions(request):
    doctor_id = request.POST['id']
    prescriptions_list_res = requests.post(PRESCRIPTION_URL + 'prescription/get_doctor_prescriptions/', {'id': doctor_id})
    prescriptions_list = prescriptions_list_res.json()['prescriptions']
    list_of_patients_ids = [str(prescription[0]) for prescription in prescriptions_list]
    patients_res = requests.post(PATIENT_URL + 'patient/get_patients/', {'ids': ",".join(list_of_patients_ids)})
    patients = {}
    for patient in patients_res.json()['patients']:
        patients[patient[0]] = patient[1]
    output = []
    for prescription in prescriptions_list:
        output.append({'patient_name': patients[prescription[0]],
                       'drugs': prescription[1],
                       'date': prescription[2]})
    return JsonResponse({'list': output}, status=HTTP_200_OK, safe=False)


@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def list_prescriptions(request):
    prescriptions_list_res = requests.post(PRESCRIPTION_URL + 'prescription/get_admin_prescriptions/', {})
    prescriptions_list = prescriptions_list_res.json()['prescriptions']
    list_of_patients_ids = [str(prescription[1]) for prescription in prescriptions_list]
    list_of_doctors_ids = [str(prescription[0]) for prescription in prescriptions_list]
    patients_res = requests.post(PATIENT_URL + 'patient/get_patients/', {'ids': ",".join(list_of_patients_ids)})
    doctors_res = requests.post(DOCTOR_URL + 'doctor/get_doctors/', {'ids': ",".join(list_of_doctors_ids)})
    patients = {}
    for patient in patients_res.json()['patients']:
        patients[patient[0]] = patient[1]
    doctors = {}
    for doctor in doctors_res.json()['doctors']:
        doctors[doctor[0]] = doctor[1]
    output = []
    for prescription in prescriptions_list:
        output.append({'doctor_name': doctors[prescription[0]],
                       'patient_name': patients[prescription[1]],
                       'drugs': prescription[2],
                       'date': prescription[3]})
    return JsonResponse({'list': output}, status=HTTP_200_OK, safe=False)


@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def list_doctors(request):
    doctors_res = requests.post(DOCTOR_URL + 'doctor/get_all_doctors/')
    doctors = doctors_res.json()['doctors']
    return JsonResponse({'doctors': doctors}, status=HTTP_200_OK, safe=False)


@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def list_patients(request):
    patients_res = requests.post(PATIENT_URL + 'patient/get_all_patients/')
    patients = patients_res.json()['patients']
    return JsonResponse({'patients': patients}, status=HTTP_200_OK, safe=False)


@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def get_daily_statistics(request):
    prescriptions_count = requests.post(PRESCRIPTION_URL + 'prescription/get_number_of_new_prescriptions/').json()['count']
    new_doctors = requests.post(DOCTOR_URL + 'doctor/get_new_doctors/').json()['doctors']
    new_patients = requests.post(PATIENT_URL + 'patient/get_new_patients/').json()['patients']
    return JsonResponse({'Prescriptions Count': prescriptions_count,
                         'New Doctors': new_doctors,
                         'New Patients': new_patients}, status=HTTP_200_OK)
