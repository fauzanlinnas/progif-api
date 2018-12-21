from rest_framework import serializers
from . models import anime
from django.contrib.auth.models import User, Group


class animeSerializer(serializers.ModelSerializer):
    class Meta:
        model= anime
        fields=('judul','tahun_tayang','musim_tayang','jumlah_episode','studio_pembuat','adaptasi','deskripsi')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
