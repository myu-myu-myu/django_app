from django.db import models
from django.core.validators import FileExtensionValidator
import os

class Music(models.Model):
    title = models.CharField(verbose_name='曲名', max_length=50)
    length = models.FloatField(verbose_name='分数', default=0.0)
    skater = models.CharField(verbose_name='名前', max_length=50)
    order = models.IntegerField(verbose_name='滑走順', default=0)
    music = models.FileField(
        verbose_name='ファイル名', 
        upload_to='music/', 
        validators=[FileExtensionValidator(['mp3', 'wav'])],)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.music.delete()
        super().delete(*args, **kwargs)

    def file_name(self):
        return os.path.basename(self.music.name)
