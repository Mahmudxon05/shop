from django.contrib.auth import login, logout, authenticate
from .serializers import *
from .models import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Create your views here.
@api_view(['POST'])
def signup(request):
    username = request.POST['username']
    password = request.POST['password']
    try:
        User.objects.create_user(username=username, password=password)
        return Response({'messega':'success'})
    except Exception as e:
        return Response(f'{e}')


@api_view(['POST'])
def log_in(request):
    username =  request.POST.get('username')
    password =  request.POST.get('password')
    usr = authenticate(username=username, password=password)
    print(usr, username,password)
    if usr is not None:
        login(request,usr)
        return Response(f'{username} logged in')
    else:
        return Response('Error username or password')
    

@api_view(['GET'])
@permission_classes([IsAuthenticated]) 
def log_out(request):
    logout(request)
    return  Response('logout')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def product(request):
    products = Product.objects.all()
    ser = ProductSerializer(products, many=True)
    return Response(ser.data)