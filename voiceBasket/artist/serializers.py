from rest_framework.serializers import ModelSerializer
from models import Request, ArtistAudio, AudioClip, ArtistRequest
from account.serializers import GenericUserSerializer


class RequestSerializer(ModelSerializer):

    class Meta:
        model = Request
        exclude = ('created_on', 'updated_on')


class AudioClipSerializer(ModelSerializer):

    class Meta:
        model = AudioClip
        exclude = ('created_on', 'updated_on')


class ArtistAudioSerializer(ModelSerializer):
    artist = GenericUserSerializer()
    audio_clip = AudioClipSerializer()

    class Meta:
        model = ArtistAudio
        exclude = ('created_on', 'updated_on')


class ArtistRequestSerializer(ModelSerializer):
    request = RequestSerializer()
    artist_audio = ArtistAudioSerializer()
    user = GenericUserSerializer()

    class Meta:
        model = ArtistRequest
        exclude = ('created_on', 'updated_on')
