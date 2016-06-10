# -*- coding: utf-8 -*-
import json
import urllib

from urllib import request, parse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from push.models import Push, User
from push.serializers import PushSerializer, UserSerializer
from django.http import HttpResponse
import logging
import http.client
"""
push message save & sending
"""


# class PushList(APIView):

# class PushList(generics.ListCreateAPIView, APIView):
class PushList(APIView):

    # queryset = Push.objects.all()
    # serializer_class = PushSerializer

    def get_token(self, name):
        try:
            return User.objects.filter(name=name).first()
        except User.DoesNotExist:
            raise Http404

    def get_publish_valid_data(self, data):
        serialized_data = PushSerializer(data=data)
        serialized_data.is_valid()
        return serialized_data.validated_data

    def post(self, request):

        validated_data = self.get_publish_valid_data(request.data)

        user_object = self.get_token(validated_data.get("target"))
        user_serializer = UserSerializer(user_object)

        token = user_serializer.data.get("token")
        name = validated_data.get("name")
        content = validated_data.get("content")
        title = validated_data.get("title")
        message = name + " : " + content

        # TODO :// Token 으로 -> FireBase
        post_data = { "data": { "title" : title, "message": message},"to" : token}

        url = "https://fcm.googleapis.com/fcm/send"

        data = parse.urlencode(post_data).encode('utf-8')

        req = urllib.request.Request(url, data=post_data)

        req.add_header('Authorization','key=AIzaSyDXKTtIPU2TmaMm0CcvHQnjQnyMyRYBDLk')

        res = urllib.request.urlopen(req)

        # rest call

        return Response()

"""
push
"""
class PushDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Push.objects.all()
    serializer_class = PushSerializer

"""
user 생성
"""
class CreateUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
