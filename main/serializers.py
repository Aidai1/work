from django.contrib.auth.models import User
from rest_framework import serializers
from .models import User_work, UserList, Organizations, Organization_defaulr_wt, Work_time


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class User_workSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_work
        fields = ('id', 'name', 'last_name', 'organization', 'login', 'passvord',)  

class OrganizationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizations
        fields =  ('id','group', 'email', ) 

class Work_TimeSerializer(serializers.ModelSerializer):
    work_time = serializers.SlugRelatedField(read_only='True', slug_field='user')
    class Meta:
        model = Work_time
        fields = ('id', 'organization', 'start_time', 'end_time','created_ad')    

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserList
        fields = ('id', 'name', 'last_name', 'organization', )
        