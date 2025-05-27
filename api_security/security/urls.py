from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import profile_view, BudgetViewSet

router = DefaultRouter()
router.register(r'budget', BudgetViewSet, basename='budget')

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('', include(router.urls)),  # include the router URLs
]
