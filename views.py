from django.shortcuts import render
from rest_framework import viewsets,generics,permissions
from models import User_work, Organizations, Organization_defaulr_wt, UserList,Work_time
from .serializers import User_workSerilizer, UserListSerilizer, Work_timeSerializer, OrganizationsSerilizer, Organization_defaulr_wtSerializer

from .permishion import IsAdminOrReadOnly, IsOwnerOrReadOnly

class User_workDetailView(generics.RetrieveAPIView):
    queryset = User_work.objects.all()
    serializer_class = User_workSerilizer
    permission_classes = (IsOwnerOrReadOnly, IsAdminOrReadOnly, )

class UserListView(generics.ListAPIView):
    queryset = UserList.objects.all()
    serializer_class = UserListSerilizer

class OrganizationView(viewsets.ModelViewSet):
    queryset = Organizations.objects.all()
    serializer_class = OrganizationsSerilizer

class Organization_defaulr_wtView(viewsets.ModelViewSet):
    queryset = Organization_defaulr_wt.objects.all()
    serializer_class = Organization_defaulr_wtSerializer

class Work_timeView(viewsets.ModelViewSet):
    queryset = Work_time.objects.all() 
    serializer_class = Work_timeSerializer


