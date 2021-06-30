from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Contact
from .serializers import ContactSerializer
from rest_framework import permissions



# Create your views here.
class ContactList(ListCreateAPIView):

    # invoca la clese contacto de serializer
    serializer_class = ContactSerializer
    #valida si esta autenticado
    permission_classes = (permissions.IsAuthenticated,)

    #define funcion para crear un contacto
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    #define funcion para buscar contactos
    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)



class ContactDetailView(RetrieveUpdateDestroyAPIView):

    # invoca la clese contacto de serializer
    serializer_class = ContactSerializer
    #valida si esta autenticado
    permission_classes = (permissions.IsAuthenticated,)
    #parametro de busqueda
    lookup_field = 'id'

    #define funcion para buscar el detalle de un contacto
    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)