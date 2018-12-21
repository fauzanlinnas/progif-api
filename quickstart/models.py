# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class anime(models.Model):
    anime_id=models.IntegerField()
    judul=models.CharField(max_length=30)
    tahun_tayang=models.IntegerField()
    musim_tayang=models.CharField(max_length=10)
    jumlah_episode=models.IntegerField()
    studio_pembuat=models.CharField(max_length=20)
    adaptasi=models.CharField(max_length=20)
    deskripsi=models.CharField(max_length=500)

    def __str__(self):
        return self.judul
