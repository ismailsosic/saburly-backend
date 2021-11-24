from django.db.models import fields
from rest_framework import serializers
from .models import Card

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = [
            'user',
            'date_from',
            'date_to',
            'description'
        ]
    def create(self, validated_data):
        """
        Create and return a new `Card` instance, given the validated data.
        """
        # safe_data = validated_data.copy()
        # safe_data[user] = 1 # dobavi iz tokena 
        return Card.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Card` instance, given the validated data.
        """
        instance.user_id = validated_data.get('user', instance.user)
        instance.date_from = validated_data.get('date_from', instance.date_from)
        instance.date_to = validated_data.get('date_to', instance.date_to)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance