# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import hashlib
import random
import string


class GenericUser(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    password = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    is_artist = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    @staticmethod
    def encrypt(password):
        salt = ''.join(c for _ in range(6) for c in random.choice(string.ascii_letters))
        password = password
        hashed = hashlib.sha1(salt + password).hexdigest()
        return salt + ":" + hashed

    @staticmethod
    def is_authenticated(supplied_password, saved_password):
        salt, digest = saved_password.split(":")
        supplied_digest = hashlib.sha1(salt + supplied_password).hexdigest()
        return supplied_digest == digest


class Session(models.Model):
    user = models.ForeignKey(GenericUser)
    session_id = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    time_to_live = models.IntegerField(default=6)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


