from .models import Task
from applications.customizing.models import UserRole
from rest_framework import serializers


class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model  = UserRole
        fields = ['role']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Task
        fields = '__all__'
        
    def validate_status(self, value):
        return value
    
    def create(self, validated_data):
        raise serializers.ValidationError({ 'status': False, 'message': 'No autorizado'})
        print(self.root.context['request'].user)
        return super().create( validated_data )
    



