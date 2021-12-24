from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import *
from system_prescription.models import Prescription


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def new_prescription(request):
    doctor_id = request.POST['doctor_id']
    patient_id = request.POST['patient_id']
    drugs = request.POST['drugs']
    date = request.POST.get('date', '0000-01-01')
    prescription = Prescription.objects.create(doctor_id=doctor_id, patient_id=patient_id, drugs=drugs, date=date)
    prescription.save()
    return JsonResponse({'message': 'Prescription added successfully!'}, status=HTTP_200_OK)