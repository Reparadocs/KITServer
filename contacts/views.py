from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from serializers import ContactSerializer
from django.contrib.auth.models import User
from models import Contact

class CreateContact(APIView):
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	permission_classes = (IsAuthenticated,)

	def post(self, request, format=None):
		serializer = ContactSerializer(data=request.data)
		if serializer.is_valid():
			contact = Contact(owner=request.user, name=serializer.data['name'], 
				phone=serializer.data['phone'], email=serializer.data['email'],
				reminder=serializer.data['reminder'])
			contact.save()
			return Response({}, status=status.HTTP_201_CREATED)
		return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class ContactList(APIView):
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	permission_classes = (IsAuthenticated,)

	def get(self, request, format=None):
		contacts = request.user.contact_set.all()
		return Response(ContactSerializer(contacts, many=True).data)
