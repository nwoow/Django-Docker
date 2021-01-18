 
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from rest_framework import generics
# from django.shortcuts import get_list_or_404
# from rest_framework.generics import ListAPIView

from .models import *
from .serializers import *

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view

from drf_yasg import openapi

# test_param = openapi.Parameter('test', openapi.IN_QUERY, description="test manual param", type=openapi.TYPE_BOOLEAN)
user_response = openapi.Response('response description', HotelSerializer)

# 'method' can be used to customize a single HTTP method of a view
@swagger_auto_schema(method='get', responses={200: user_response})
# 'methods' can be used to apply the same modification to multiple methods
@swagger_auto_schema(methods=['post'], request_body=HotelSerializer)
@api_view(['GET','POST'])
def api_hotel_list_view(request):
    hotel=Hotel.objects.all()
    if request.method =='GET':
        serializer=HotelSerializer(hotel,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        # data={}
        serializer=HotelSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            # return 'created Successfully'
            return Response(serializer.data)   
        else:
            # return 'Creation not succesfull'
            return Response(serializer.error)

user_response = openapi.Response('response description', RoomSerializer)

# 'method' can be used to customize a single HTTP method of a view
@swagger_auto_schema(method='get', responses={200: user_response})
# 'methods' can be used to apply the same modification to multiple methods
@swagger_auto_schema(methods=['post'], request_body=RoomSerializer)

@api_view(['GET','POST']) 
def api_room_list_view(request):
    room=Room.objects.all()
    if request.method=='GET':
        serializer=RoomSerializer(room,many=True)
        return Response(serializer.data)

    if request.method=='POST':
        serializer=RoomSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(request.data)
        else:
            return Response(serializer.error)


user_response = openapi.Response('response description', GuestSerializer)

# 'method' can be used to customize a single HTTP method of a view
@swagger_auto_schema(method='get', responses={200: user_response})
# 'methods' can be used to apply the same modification to multiple methods
@swagger_auto_schema(methods=['post'], request_body=GuestSerializer)
@api_view(['GET','POST'])
def api_guest_list_view(request):
    guest=Guest.objects.all()
    if request.method=='GET':
        serializer=GuestSerializer(guest,many=True)
        return Response(serializer.data)
    if request.method =='POST':
        serializer=GuestSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.error)    


user_response = openapi.Response('response description', BookingSerializer)

# 'method' can be used to customize a single HTTP method of a view
@swagger_auto_schema(method='get', responses={200: user_response})
# 'methods' can be used to apply the same modification to multiple methods
@swagger_auto_schema(methods=['post'], request_body=BookingSerializer)                
@api_view(['GET','POST'])
def api_booking_list_view(request):
    booking=Booking.objects.all()
    if request.method =='GET':
        serializer=BookingSerializer(booking,many=True)
        return Response(serializer.data)
    if request.methos=='POST':
        serializer=BookingSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.error) 