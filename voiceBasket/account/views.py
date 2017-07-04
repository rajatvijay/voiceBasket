# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.views import APIView

from voiceBasket.response import *
from voiceBasket.APIPermissions import AuthToken
from models import GenericUser, Session
from serializers import GenericUserSerializer
from artist.serializers import ArtistRequestSerializer, RequestSerializer
from artist.models import ArtistRequest, Request

import hashlib
import os


class GenericUserView(APIView):

    # Login
    def put(self, request):
        validated_data = request.data
        email = validated_data['email']
        password = validated_data['password']
        if GenericUser.objects.filter(email=email).first():
            user = GenericUser.objects.filter(email=email).first()
            if GenericUser.is_authenticated(password, user.password):
                session = Session(user=user,
                                  session_id=str(hashlib.sha1(os.urandom(128)).hexdigest())[:32])
                session.save()
                GENERAL_MESSAGE['result'] = {
                    'session_id': session.session_id,
                    'user': GenericUserSerializer(instance=user).data
                }

                GENERAL_MESSAGE['message'] = 'User Logged in Successfully'
                return JSONResponse(GENERAL_MESSAGE)
            else:
                return JSONResponse(AUTHENTICATION_ERROR)
        else:
            return JSONResponse(AUTHENTICATION_ERROR)

    # Register
    def post(self, request):
        validated_data = request.data

        if GenericUser.objects.filter(email=validated_data['email']).first():
            return JSONResponse(ALREADY_REGISTERED)

        password = validated_data['password']
        del (validated_data['password'])
        user = GenericUser(password=GenericUser.encrypt(password),
                           **validated_data)
        user.save()

        session = Session(user=user,
                          session_id=str(hashlib.sha1(os.urandom(128)).hexdigest())[:32])
        session.save()

        GENERAL_MESSAGE['result'] = {
            'user': GenericUserSerializer(instance=user).data,
            'session_id': session.session_id
        }
        GENERAL_MESSAGE['message'] = 'User Registered Successfully'
        return JSONResponse(GENERAL_MESSAGE)


class DashboardView(APIView):
    permission_classes = (AuthToken, )

    def get(self, request):
        user = request.user
        requests_list = Request.objects.filter(artistrequest__user=user)
        # artist_request = ArtistRequest.objects.filter(user=user)
        if not requests_list:
            return JSONResponse('error')

        GENERAL_MESSAGE['result'] = {
            'artist_request': RequestSerializer(instance=requests_list, many=True).data
        }
        GENERAL_MESSAGE['message'] = 'Dashboard fetched successfully'

        return JSONResponse(GENERAL_MESSAGE)


class AcceptRejectRequest(APIView):
    permission_classes = (AuthToken, )

    def put(self, request):
        req = Request.objects.get(pk=request.data['id'])
        req.user_status = request.data['user_response']
        req.save()

        GENERAL_MESSAGE['result'] = {
            'artist_request': RequestSerializer(instance=Request.objects.filter(artistrequest__user=request.user),
                                                many=True).data
        }

        GENERAL_MESSAGE['message'] = 'Status updated successfully!'

        return JSONResponse(GENERAL_MESSAGE)
