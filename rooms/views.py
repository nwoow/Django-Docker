 
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
            return Response(data,status=status.HTTP_201_CREATED)   
        else:
            # return 'Creation not succesfull'
            return Response(serializer.error,status=status.HTTP_404_NOT_FOUND)

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
            return Response(data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error,status=status.HTTP_404_NOT_FOUND)

@api_view(['GET','POST'])
def api_guest_list_view(request):
    guest=Guest.objects.all()
    if request.method=='GET':
        serializer=GuestSerializer(guest,many=True)
        return Response(serializer.data)
    if request.method =='POST':
        serializer=GuestSerializer(data=request.data)
        if serializer.is_valid():
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error, status=status.HTTP_404_NOT_FOUND)                    
@api_view(['GET','POST'])
def api_booking_list_view(request):
    booking=Booking.objects.all()
    if request.method =='GET':
        serializer=BookingSerializer(booking,many=True)
        return Response(serializer.data)
    if request.methos=='POST':
        serializer=BookingSerializer(data=request.data)
        if serializer.is_valid():
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error, status=status.HTTP_404_NOT_FOUND) 