from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import *
from system_prescription.models import Prescription
from django.utils.timezone import datetime


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def new_prescription(request):
    doctor_id = request.POST['doctor_id']
    patient_id = request.POST['patient_id']
    drugs = request.POST['drugs']
    date = request.POST.get('date', datetime.now().strftime('%Y-%m-%d'))
    prescription = Prescription.objects.create(doctor_id=doctor_id,
                                               patient_id=patient_id,
                                               drugs=drugs,
                                               date=date)
    prescription.save()
    return JsonResponse({'message': 'Prescription added successfully!'}, status=HTTP_200_OK)


@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def get_patient_prescriptions(request):
    patient_id = request.POST['id']
    prescriptions = list(Prescription.objects.filter(patient_id=patient_id).values_list('doctor_id', 'drugs', 'date'))
    return JsonResponse({'prescriptions': prescriptions}, status=HTTP_200_OK, safe=False)


@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def get_doctor_prescriptions(request):
    doctor_id = request.POST['id']
    prescriptions = list(Prescription.objects.filter(doctor_id=doctor_id).values_list('patient_id', 'drugs', 'date'))
    return JsonResponse({'prescriptions': prescriptions}, status=HTTP_200_OK, safe=False)


@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def get_admin_prescriptions(request):
    prescriptions = list(Prescription.objects.all().values_list('doctor_id', 'patient_id', 'drugs', 'date'))
    return JsonResponse({'prescriptions': prescriptions}, status=HTTP_200_OK, safe=False)


@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def get_number_of_new_prescriptions(request):
    prescriptions = Prescription.objects.filter(date=datetime.now().strftime('%Y-%m-%d'))
    return JsonResponse({'count': len(prescriptions)}, status=HTTP_200_OK, safe=False)
