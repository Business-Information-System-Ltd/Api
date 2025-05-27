from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Budget


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']

class BudgetSerializer(serializers.ModelSerializer):
    BudgetCode = serializers.CharField(source='Budget_code')
    BudgetName = serializers.CharField(source='Budget_name')
    class Meta:
        model = Budget
        fields = ['BudgetCode','BudgetName']