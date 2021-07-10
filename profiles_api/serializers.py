from rest_framework import serializers
 

class HelloSerializer(serializers.Serializer):
    """Serializers a field for testing our API views"""
    name = serializers.CharField(max_length=10)

