from rest_framework import serializers
from django.core.validators import validate_email
from django.core.exceptions import ValidationError as DjangoValidationError
from .tasks import send_email_task


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self, attrs):
        email = attrs.get('email')
        if not email:
            raise serializers.ValidationError({'email': 'Email is required'})

        try:
            validate_email(email)
        except DjangoValidationError:
            raise serializers.ValidationError({'email': 'Invalid email format'})

        return attrs

    def create(self, validated_data):
        email = validated_data.get('email')

        subject = 'Sent Email with Celery Task'
        message = 'How are you?'
        recipient_list = [email]

        # Send the email asynchronously using Celery
        send_email_task.delay(subject, message, recipient_list)

        return validated_data
