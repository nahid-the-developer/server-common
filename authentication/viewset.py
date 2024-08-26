from rest_framework import viewsets
from rest_framework.response import Response
from common.viewsets import BaseModelViewSet
from common.serializers import EmptySerializer


class AuthenticationViewSet(BaseModelViewSet):
    serializer_class = EmptySerializer

    def list(self, request):
        return Response({'message': 'Hello'})
