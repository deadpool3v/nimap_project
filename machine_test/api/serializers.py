from rest_framework import serializers
from .models import Client, Project
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()  
    projects = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'projects', 'created_at', 'created_by']

class ProjectSerializer(serializers.ModelSerializer):
    client = ClientSerializer()  
    users = UserSerializer(many=True)  
    created_by = serializers.StringRelatedField()  

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'created_at', 'created_by']
