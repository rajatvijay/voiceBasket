from rest_framework.serializers import ModelSerializer
from models import GenericUser


class GenericUserSerializer(ModelSerializer):

    class Meta:
        model = GenericUser
        exclude = ('password', )
