from django.contrib.auth.models import User, Group
from be_paletter.models import Palettes
from rest_framework import serializers

# serializers define the API representation


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class PalettesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        required=True, allow_blank=False, max_length=200)
    image = serializers.ImageField()
    source = serializers.URLField()
    source_string = serializers.CharField(
        required=False, allow_blank=True, max_length=200)

    def create(self, palette_data):
        return Palettes.create(**palette_data)

