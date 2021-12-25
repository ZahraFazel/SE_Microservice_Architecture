from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import *
from system_doctor.models import Doctor
from django.utils.timezone import datetime


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def signup(request):
    name = request.POST['name']
    national_code = request.POST['national_code']
    password = request.POST['password']
    try:
        doctor = Doctor.objects.create(name=name,
                                       national_code=national_code,
                                       signup_date=datetime.now().strftime('%Y-%m-%d'),
                                       username=name + str(national_code))
        doctor.set_password(password)
        doctor.save()
        token = Token.objects.create(user=doctor)
        return JsonResponse({'token': token.key}, status=HTTP_201_CREATED)
    except:
        return JsonResponse({'error': 'This national code has registered before.'}, status=HTTP_500_INTERNAL_SERVER_ERROR)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    name = request.data.get('name')
    national_code = request.data.get('national_code')
    password = request.data.get('password')
    username = name + str(national_code)
    if username is None or password is None:
        return JsonResponse({'error': 'Name, national code or password is wrong!'}, status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return JsonResponse({'error': 'Access denied!'}, status=HTTP_404_NOT_FOUND)
    token = Token.objects.get_or_create(user=user)[0]
    return JsonResponse({'token': token.key}, status=HTTP_200_OK)


@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def validate_with_token(request):
    token = request.POST['token']
    try:
        id = Token.objects.filter(key=token)[0].user_id
        doctor = Doctor.objects.filter(user_ptr_id=id)
        if len(doctor) > 0:
            return JsonResponse({'id': doctor[0].user_ptr_id}, status=HTTP_200_OK)
        else:
            return JsonResponse({}, status=HTTP_403_FORBIDDEN)
    except:
        return JsonResponse({}, status=HTTP_403_FORBIDDEN)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def get_doctors(request):
    ids = request.POST['ids'].split(",")
    doctors = list(Doctor.objects.filter(user_ptr_id__in=ids).values_list('user_ptr_id', 'name'))
    return JsonResponse({'doctors': doctors}, status=HTTP_200_OK, safe=False)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def get_all_doctors(request):
    doctors = list(Doctor.objects.all().values_list('name', flat=True))
    return JsonResponse({'doctors': doctors}, status=HTTP_200_OK, safe=False)


@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def get_new_doctors(request):
    doctors = list(Doctor.objects.filter(signup_date=datetime.now().strftime('%Y-%m-%d')).values_list('name', flat=True))
    return JsonResponse({'doctors': doctors}, status=HTTP_200_OK, safe=False)


@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def profile(request):
    token = request.POST['token']
    try:
        id = Token.objects.filter(key=token)[0].user_id
        doctor = Doctor.objects.filter(user_ptr_id=id)
        if len(doctor) > 0:
            return JsonResponse({'name': doctor[0].name,
                                 'national_code': doctor[0].national_code,
                                 'username': doctor[0].username}, status=HTTP_200_OK)
        else:
            return JsonResponse({}, status=HTTP_403_FORBIDDEN)
    except:
        return JsonResponse({}, status=HTTP_403_FORBIDDEN)
