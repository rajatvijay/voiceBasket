# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.views import APIView

from voiceBasket.response import *
from voiceBasket.constants import GENDER_OPTIONS, LANGUAGE_OPTIONS, VOICE_OVER_TYPE, AGE_TYPE
from voiceBasket.APIPermissions import AuthToken
from serializers import ArtistRequestSerializer, ArtistAudioSerializer
from models import Request, Characters, ArtistRequest, ArtistAudio


class RequestView(APIView):
    permission_classes = (AuthToken, )

    def post(self, request):
        validated_data = request.data
        new_request = Request(**validated_data['request'])
        new_request.save()

        if new_request.has_characters:
            for char in validated_data['characters']:
                    character = Characters(request=new_request, **char)
                    character.save()

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
            'gender': GENDER_OPTIONS,
            'language': LANGUAGE_OPTIONS,
            'voice_over_type': VOICE_OVER_TYPE,
            'age_type': AGE_TYPE
        }
        GENERAL_MESSAGE['message'] = 'The list has been fetched successfully'

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
