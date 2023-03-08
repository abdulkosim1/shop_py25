from rest_framework.serializers import ModelSerializer, EmailField, ValidationError
from spam.models import Contact


class ContactSerializer(ModelSerializer):
    email = EmailField(required=False)

    class Meta:
        model = Contact
        fields = '__all__'

    def create(self, validated_data):
        if Contact.objects.filter(email=validated_data['email']).exists():
            raise ValidationError('вы уже подписались')
        return super().create(validated_data)
    