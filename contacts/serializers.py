from rest_framework.serializers import ModelSerializer
from .models import Contact


class ContactSerializer(ModelSerializer):

    # define los datos del modelo
    class Meta:
        model = Contact
        fields = ['first_name', 'id', 'last_name', 'country_code', 'phone_number', 'contact_picture', 'is_favourite']