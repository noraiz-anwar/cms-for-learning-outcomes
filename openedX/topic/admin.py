# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from topic.models import Topic

class TopicAdmin(admin.ModelAdmin):
    pass
admin.site.register(Topic, TopicAdmin)
