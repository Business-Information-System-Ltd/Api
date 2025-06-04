from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer,BudgetSerializer
from .models import Budget
from rest_framework import viewsets
from rest_framework.permissions import AllowAny



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({"message": "Hello, you are authenticated!"})

    
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def profile_view(request):
#     serializer = UserSerializer(request.user)
#     return Response(serializer.data)

    
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def profile_view(request):
    if request.method == 'GET':
        users=User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({
            "username": user.username,
            "email": user.email,
            "role": user.role  
        })

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(serializer.validated_data['password'])  # Ensure password is hashed
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# @permission_classes([AllowAny])
# def register_user(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def budget_view(request):
    if request.method == 'GET':    
       budgets = Budget.objects.all()
       serializer = BudgetSerializer(budgets, many=True)
       return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BudgetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({"detail": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


    def callback_view(request):
        code = request.GET.get('code')
        return HttpResponse(f"Authorization Code: {code}")




