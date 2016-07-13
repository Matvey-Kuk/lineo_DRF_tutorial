from __future__ import unicode_literals

from django.db import models


class CatModel(models.Model):
    name = models.CharField(max_length=1000, verbose_name='Name')
    width = models.IntegerField(verbose_name='Width')
    height = models.IntegerField(verbose_name='Height')
    length = models.IntegerField(verbose_name='Height')

    class Meta:
        verbose_name = 'Cat'
        verbose_name_plural = 'Cats'

    def __str__(self):
        return self.name

    def volume(self):
        """
        :return: Cat's volume
        """
        return self.width * self.length * self.height