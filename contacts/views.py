from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from serializers import ContactSerializer, ContactListSerializer
from django.contrib.auth.models import User
from models import Contact
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

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
			return Response({'success': True}, status=status.HTTP_201_CREATED)
		return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class EditContact(APIView):
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	permission_classes = (IsAuthenticated,)

	def get_object(self, request, pk):
		try:
			contact = Contact.objects.get(pk=pk)
			if contact.owner == request.user:
				return contact
			else:
				return None
		except Contact.DoesNotExist:
			raise Http404

	def post(self, request, pk, format=None):
		contact = self.get_object(request, pk)
		if not contact:
			return Response('Not Owner', status=status.HTTP_400_BAD_REQUEST)
		serializer = ContactSerializer(data=request.data)
		if serializer.is_valid():
			contact.name = serializer.data['name']
			contact.phone = serializer.data['phone']
			contact.email = serializer.data['email']
			contact.reminder = serializer.data['reminder']
			contact.save()
			return Response({'success': True})
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteContact(APIView):
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	permission_classes = (IsAuthenticated,)

	def get_object(self, request, pk):
		try:
			contact = Contact.objects.get(pk=pk)
			if contact.owner == request.user:
				return contact
			else:
				return None
		except Contact.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		contact = self.get_object(request, pk)
		if not contact:
			return Response('Not Owner', status=status.HTTP_400_BAD_REQUEST)
		contact.delete()
		return Response({'success': True})

class ContactList(APIView):
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	permission_classes = (IsAuthenticated,)

	def get(self, request, format=None):
		contacts = request.user.contact_set.all()
		return Response(ContactListSerializer(contacts, many=True).data)
