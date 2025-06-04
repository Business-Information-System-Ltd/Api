from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import profile_view, BudgetViewSet
from django.http import HttpResponse



def oauth_callback(request):
    return HttpResponse("OK! You are Successfully. OAuth callback handled")

router = DefaultRouter()
router.register(r'budget', BudgetViewSet, basename='budget')




urlpatterns = [
    path('profile/', profile_view, name='profile'),
    # path('register/', register_user, name='register-user'),
    path('', include(router.urls)),  
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('oauth/callback/', oauth_callback),
]
