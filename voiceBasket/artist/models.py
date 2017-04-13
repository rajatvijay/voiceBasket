# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from voiceBasket import constants
from account.models import GenericUser

import uuid


class AudioClip(models.Model):
    GENDER = constants.make_choices(constants.GENDER_OPTIONS)
    LANGUAGE = constants.make_choices(constants.LANGUAGE_OPTIONS)
    VOICE_OVER_TYPE = constants.make_choices(constants.VOICE_OVER_TYPE)
    AGE_RANGE = constants.make_choices(constants.AGE_TYPE)

    url = models.URLField()
    code = models.UUIDField(default=uuid.uuid4)
    gender = models.CharField(max_length=50, choices=GENDER)
    language = models.CharField(max_length=50, choices=LANGUAGE)
    age_range = models.CharField(max_length=50, choices=AGE_RANGE)
    voice_over_type = models.CharField(max_length=50, choices=VOICE_OVER_TYPE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class ArtistAudio(models.Model):
    artist = models.ForeignKey(GenericUser)
    audio_clip = models.ForeignKey(AudioClip)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class Request(models.Model):
    REQUEST_TYPES = constants.make_choices(constants.REQUEST_TYPE)

    type = models.CharField(max_length=50, choices=REQUEST_TYPES)
    duration_in_minutes = models.IntegerField()
    word_count = models.IntegerField()
    script_text = models.CharField(max_length=1000)
    script_url = models.URLField()
    additional_notes = models.CharField(max_length=500)
    has_characters = models.BooleanField(default=False)
    reference_file_url = models.URLField()
    audio_book_name = models.CharField(max_length=200)
    ivr_count = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class Characters(models.Model):
    request = models.ForeignKey(Request)
    artist_audio = models.ForeignKey(ArtistAudio)
    weightage = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class ArtistRequest(models.Model):
    request = models.ForeignKey(Request)
    artist_audio = models.ForeignKey(ArtistAudio)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

