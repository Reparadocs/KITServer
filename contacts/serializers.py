from rest_framework import serializers

class ContactSerializer(serializers.Serializer):
	name = serializers.CharField(max_length=100)
	phone = serializers.CharField(max_length=100, allow_blank=True)
	email = serializers.CharField(max_length=100, allow_blank=True)
	reminder = serializers.IntegerField()

class ContactListSerializer(serializers.Serializer):
	id = serializers.IntegerField()
	name = serializers.CharField(max_length=100)
	phone = serializers.CharField(max_length=100, allow_blank=True)
	email = serializers.CharField(max_length=100, allow_blank=True)
	reminder = serializers.IntegerField()