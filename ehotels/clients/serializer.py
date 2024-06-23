from rest_framework import serializers
from .models import Client,Room,Booking


class client(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        
        

class room(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
                
                
                

class room(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
                                