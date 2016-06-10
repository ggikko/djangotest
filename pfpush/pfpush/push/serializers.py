# -*- coding: utf-8 -*-

from django.forms import widgets
from rest_framework import serializers
from push.models import Push, LANGUAGE_CHOICES, STYLE_CHOICES, User


class PushSerializer(serializers.Serializer):

    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True, max_length=10)
    target = serializers.CharField(required=False, allow_blank=True, max_length=10)
    title = serializers.CharField(style={'base_template': 'textarea.html'})
    content = serializers.CharField(style={'base_template': 'textarea.html'})

    def create(self, validated_data):
        """
        검증한 데이터로 새 `Push` 인스턴스를 생성하여 리턴합니다.
        """
        return Push.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        검증한 데이터로 기존 `Push` 인스턴스를 업데이트한 후 리턴합니다.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.target = validated_data.get('target', instance.target)
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance

class UserSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True, max_length=10)
    token = serializers.CharField(required=False, allow_blank=True, max_length=500)

    def create(self, validated_data):
        """
        검증한 데이터로 새 `User` 인스턴스를 생성하여 리턴합니다.
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):

        """
        검증한 데이터로 기존 `User` 인스턴스를 업데이트한 후 리턴합니다.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.token = validated_data.get('token', instance.token)
        instance.save()
        return instance