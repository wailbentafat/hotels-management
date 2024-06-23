from .models import Client,Room,Booking
from .serializer import client,room
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from datetime import date
from django.contrib.auth.permission import isadmin

@api_view(['POST'])
def add_client(request):
    serializers=client(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data,status=status.HTTP_201_CREATED)
    return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_client(request,name):
    client=Client.objects.get(name=name)
    client.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

#@api_view(['PUT'])
#def prolonge_date(request,name):
 #   client=Client.object.get(name=name)
  #  if serializer.is_valid():
   #   serializer.save()
     #   return Response(serializer.data,status=status.HTTP_201_CREATED)
    #return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])

def get_empty_room(request,name):
  rooms=Room.objects.filter(free=True)
  return Response(rooms)

@api_view(['POST'])
@permission_classes([isadmin])
def add_room(request):
    serializers=room(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data,status=status.HTTP_201_CREATED)
    return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def book(request):
    

    

##signals to end date automatically