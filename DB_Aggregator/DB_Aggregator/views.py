import requests
from django.http import JsonResponse
from rest_framework.decorators import renderer_classes, api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.status import HTTP_200_OK

from DB_Aggregator.settings import ADMIN_URL, PATIENT_URL, DOCTOR_URL, PRESCRIPTION_URL


@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def list_patient_prescriptions(request):
    patient_id = request.POST['id']
    prescriptions_list_res = requests.post(PRESCRIPTION_URL + 'prescription/get_patient_prescriptions/', {'id': patient_id})
    prescriptions_list = prescriptions_list_res.json()
    list_of_doctors_ids = [str(prescription['doctor_id']) for prescription in prescriptions_list]
    doctors_res = requests.post(DOCTOR_URL + 'doctor/get_doctors/', {'ids': ",".join(list_of_doctors_ids)})
    doctors = {}
    for doctor in doctors_res.json():
        doctors[doctor['user_ptr_id']] = doctor['name']
    output = []
    for prescription in prescriptions_list:
        output.append({'doctor_name': doctors[prescription['doctor_id']],
                       'drugs': prescription['drugs'],
                       'date': prescription['date']})
    return JsonResponse({'list': output}, status=HTTP_200_OK, safe=False)

@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def list_doctor_prescriptions(request):
    doctor_id = request.POST['id']
    prescriptions_list_res = requests.post(PRESCRIPTION_URL + 'prescription/get_doctor_prescriptions/', {'id': doctor_id})
    prescriptions_list = prescriptions_list_res.json()
    list_of_patients_ids = [str(prescription['patient_id']) for prescription in prescriptions_list]
    patients_res = requests.post(PATIENT_URL + 'patient/get_patients/', {'ids': ",".join(list_of_patients_ids)})
    patients = {}
    for patient in patients_res.json():
        patients[patient['user_ptr_id']] = patient['name']
    output = []
    for prescription in prescriptions_list:
        output.append({'patient_name': patients[prescription['patient_id']],
                       'drugs': prescription['drugs'],
                       'date': prescription['date']})
    return JsonResponse({'list': output}, status=HTTP_200_OK, safe=False)



@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def list_admin_prescriptions(request):
    prescriptions_list_res = requests.post(PRESCRIPTION_URL + 'prescription/get_admin_prescriptions/', {})
    prescriptions_list = prescriptions_list_res.json()
    list_of_patients_ids = [str(prescription['patient_id']) for prescription in prescriptions_list]
    list_of_doctors_ids = [str(prescription['doctor_id']) for prescription in prescriptions_list]
    patients_res = requests.post(PATIENT_URL + 'patient/get_patients/', {'ids': ",".join(list_of_patients_ids)})
    doctors_res = requests.post(DOCTOR_URL + 'doctor/get_doctors/', {'ids': ",".join(list_of_doctors_ids)})
    patients = {}
    for patient in patients_res.json():
        patients[patient['user_ptr_id']] = patient['name']

    doctors = {}
    for doctor in doctors_res.json():
        doctors[doctor['user_ptr_id']] = doctor['name']

    output = []
    for prescription in prescriptions_list:
        output.append({'patient_name': patients[prescription['patient_id']],
                       'doctor_name': doctors[prescription['doctor_id']],
                       'drugs': prescription['drugs'],
                       'date': prescription['date']})
    return JsonResponse({'list': output}, status=HTTP_200_OK, safe=False)
