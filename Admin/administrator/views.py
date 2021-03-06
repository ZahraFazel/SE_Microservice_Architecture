from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK, HTTP_403_FORBIDDEN
from administrator.models import SystemAdmin


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return JsonResponse({'error': 'Username or password is wrong!'}, status=HTTP_400_BAD_REQUEST)
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
        admin = SystemAdmin.objects.filter(user_ptr_id=id)
        if len(admin) > 0:
            return JsonResponse({'id': admin[0].user_ptr_id}, status=HTTP_200_OK)
        else:
            return JsonResponse({}, status=HTTP_403_FORBIDDEN)
    except:
        return JsonResponse({}, status=HTTP_403_FORBIDDEN)


@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def profile(request):
    token = request.POST['token']
    try:
        id = Token.objects.filter(key=token)[0].user_id
        admin = SystemAdmin.objects.filter(user_ptr_id=id)
        if len(admin) > 0:
            return JsonResponse({'name': admin[0].name,
                                 'national_code': admin[0].national_code,
                                 'username': admin[0].username}, status=HTTP_200_OK)
        else:
            return JsonResponse({}, status=HTTP_403_FORBIDDEN)
    except:
        return JsonResponse({}, status=HTTP_403_FORBIDDEN)
