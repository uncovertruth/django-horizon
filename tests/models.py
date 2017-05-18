# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.db import models
from django.conf import settings

from horizon.models import (
    AbstractHorizontalMetadata,
    AbstractHorizontalModel,
)


class HorizontalMetadata(AbstractHorizontalMetadata):
    pass


class HorizonParent(AbstractHorizontalModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    spam = models.CharField(max_length=15)

    class Meta(object):
        horizontal_group = 'a'
        horizontal_key = 'user'


class HorizonChild(AbstractHorizontalModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    parent = models.ForeignKey(HorizonParent, on_delete=models.CASCADE)

    class Meta(object):
        horizontal_group = 'a'
        horizontal_key = 'user'


class AnotherGroup(AbstractHorizontalModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    egg = models.CharField(max_length=15)

    class Meta(object):
        horizontal_group = 'b'
        horizontal_key = 'user'
