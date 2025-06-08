from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Budget, CustomerUser

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomerUser
        fields = ['id', 'username', 'email', 'password', 'role']

    def create(self, validated_data):
        user = CustomerUser(
            username=validated_data['username'],
            email=validated_data.get('email'),
            role=validated_data.get('role', 'staff')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class BudgetSerializer(serializers.ModelSerializer):
    BudgetCode = serializers.CharField(source='Budget_code')
    BudgetName = serializers.CharField(source='Budget_name')
    class Meta:
        model = Budget
        fields = ['BudgetCode','BudgetName']