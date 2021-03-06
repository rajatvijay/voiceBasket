# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.views import APIView

from voiceBasket.response import *
from voiceBasket.constants import GENDER_OPTIONS, LANGUAGE_OPTIONS, VOICE_OVER_TYPE, \
    AGE_RANGE, ARTIST_PASSWORD, ARTIST_MOBILE, ARTIST_COMPANY_NAME
from voiceBasket.APIPermissions import AuthToken
from serializers import ArtistRequestSerializer, ArtistAudioSerializer
from models import Request, Characters, ArtistRequest, ArtistAudio, AudioClip
from account.models import GenericUser, Session
from account.serializers import GenericUserSerializer
from voiceBasket.constants import ADMIN_EMAIL

import hashlib
import os


class RequestView(APIView):
    permission_classes = (AuthToken, )

    def post(self, request):
        validated_data = request.data

        print(validated_data)

        validated_data = JSONResponse.convert_json(validated_data, JSONResponse.camel_to_underscore)

        print(validated_data)

        new_request = Request(**validated_data['request'])
        new_request.save()

        # If the request has characters
        # create entry in request table
        if new_request.has_characters:
            for char in validated_data['characters']:
                    character = Characters(request=new_request, artist_audio_id=char['id'])
                    character.save()

        # Add entry in the ArtistRequest table
        artist_requests = []
        for artist in validated_data['artist_request']:
            artist_request = ArtistRequest(user=request.user, request=new_request,
                                           artist_audio_id=artist['artist']['id'])
            artist_request.save()
            artist_requests.append(artist_request)

        GENERAL_MESSAGE['result'] = {
            'artist_request': ArtistRequestSerializer(instance=artist_requests, many=True).data
        }
        GENERAL_MESSAGE['message'] = 'The request has been received successfully'
        return JSONResponse(GENERAL_MESSAGE)


class OptionsView(APIView):

    def get(self, request):
        GENERAL_MESSAGE['result'] = {
            '0__language': LANGUAGE_OPTIONS,
            '3__age_range': AGE_RANGE,
            '2__voice_over_type': VOICE_OVER_TYPE,
            '1__gender': GENDER_OPTIONS
        }
        GENERAL_MESSAGE['message'] = 'The list has been fetched successfully!'

        return JSONResponse(GENERAL_MESSAGE)


class SearchView(APIView):

    def get(self, request):
        artist_audios = ArtistAudio.objects.all()

        # TODO: Return something useful or meaningful
        if not artist_audios:
            return JSONResponse("Error")

        GENERAL_MESSAGE['result'] = {
            'artist_audio': ArtistAudioSerializer(instance=artist_audios, many=True).data
        }
        GENERAL_MESSAGE['message'] = 'The artist and their audio clips has been fetched successfully'

        return JSONResponse(GENERAL_MESSAGE)


# Of no use since using user's login view
class ArtistView(APIView):
    permission_classes = (AuthToken, )

    # Register Artist
    def post(self, request):
        user = request.user
        validated_data = request.data

        if not user.email == ADMIN_EMAIL:
            return JSONResponse(AUTHENTICATION_ERROR)

        if GenericUser.objects.filter(email=validated_data['email']).first():
            return JSONResponse(ALREADY_REGISTERED)

        artist = GenericUser(password=GenericUser.encrypt(ARTIST_PASSWORD),
                             mobile=ARTIST_MOBILE, company_name=ARTIST_COMPANY_NAME,
                             is_artist=True, **validated_data)
        artist.save()

        session = Session(user=artist,
                          session_id=str(hashlib.sha1(os.urandom(128)).hexdigest())[:32])
        session.save()

        GENERAL_MESSAGE['result'] = {
            'investor': GenericUserSerializer(instance=artist).data,
            'session_id': session.session_id
        }
        GENERAL_MESSAGE['message'] = 'Artist Registered Successfully'
        return JSONResponse(GENERAL_MESSAGE)


class AudioView(APIView):
    permission_classes = (AuthToken, )

    def post(self, request):
        user = request.user

        if user.user_type != 'artist':
            return JSONResponse(AUTHENTICATION_ERROR)

        validated_data = request.data

        audio_clip = AudioClip(**validated_data)
        audio_clip.save()

        artist_audio = ArtistAudio(artist=user, audio_clip=audio_clip)
        artist_audio.save()

        GENERAL_MESSAGE['result'] = {
            'artist_audio': ArtistAudioSerializer(instance=artist_audio).data
        }
        GENERAL_MESSAGE['message'] = 'Artist audio added successfully'

        return JSONResponse(GENERAL_MESSAGE)
