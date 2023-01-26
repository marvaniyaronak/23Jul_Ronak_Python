from django.shortcuts import render
from django.http import HttpResponse
from .models import user_info
from .serializers import user_serializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.

@api_view(['GET'])
def getdata(request):
    if request.method=='GET':
        usr=user_info.objects.all()
        usr_sl=user_serializer(usr,many=True)
        return Response(usr_sl.data,status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT'])
def get_uid(request,id):
    try:
        uid=user_info.objects.get(id=id)
    except user_info.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    uslr=user_serializer(uid)
    if request.method=='PUT':
        updat=user_serializer(uid,data=request.data)
        if updat.is_valid():
            updat.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(uslr.data,status=status.HTTP_200_OK)


@api_view(['PUT'])
def updatedata(request,id):
    try:
        uid=user_info.objects.get(id=id)
    except user_info.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='PUT':
        updat=user_serializer(uid,data=request.data)
        if updat.is_valid():
            updat.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def savedata(request):
    if request.method=='POST':
        newusr=user_serializer(data=request.data)
        if newusr.is_valid():
            newusr.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


def deletedata(request,id):
    try:
        uid=user_info.objects.get(id=id)
    except user_info.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    user_info.delete(uid)
    return Response(status=status.HTTP_200_OK)