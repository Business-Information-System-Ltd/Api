from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import AnonymousUser
from .models import ApiKey

class GlobalAPIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Api-Key '):
            return None

        try:
            api_key = auth_header.split(' ')[1] 
        except IndexError:
            raise AuthenticationFailed('Invalid API Key header format.')

        try:
            key_obj = ApiKey.objects.get(key=api_key, is_active=True)
        except ApiKey.DoesNotExist:
            raise AuthenticationFailed('Invalid or inactive API Key')

        return (AnonymousUser(), None)