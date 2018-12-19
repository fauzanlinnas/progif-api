from rest_framework import serializers
from . models import anime


class animeSerializer(serializers.ModelSerializer):
    class Meta:
        model= anime
        fields=('judul','tahun_tayang','musim_tayang','jumlah_episode','studio_pembuat','adaptasi','deskripsi')
