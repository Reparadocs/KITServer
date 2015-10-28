from rest_framework import serializers

class FacebookSerializer(serializers.Serializer):
	accessToken = serializers.CharField(max_length=250)

class UserSerializer(serializers.Serializer):
	username = serializers.CharField(max_length=100)
	password = serializers.CharField(max_length=100)