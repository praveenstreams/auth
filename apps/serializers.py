from rest_framework import serializers
from django.contrib.auth.models import User



class UserData(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password','email','phone','place']


    phone=serializers.CharField(max_length=100,source='get_profile.phone')
    place = serializers.CharField(max_length=100, source='get_profile.place')




