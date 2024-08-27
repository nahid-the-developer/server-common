from rest_framework.response import Response
from common.viewsets import BaseModelViewSet
from rest_framework import status
from rest_framework.decorators import action
from common.serializers import EmptySerializer
from authentication.serializers import EmailSerializer


class AuthenticationViewSet(BaseModelViewSet):
    serializer_class = EmptySerializer

    def list(self, request):
        return Response({'message': 'Hello'})

    @action(detail=False, methods=['POST'], url_path='sent_email')
    def sent_mail(self, request, *args, **kwargs):
        serializer = EmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Email sent successfully'}, status=status.HTTP_200_OK)
