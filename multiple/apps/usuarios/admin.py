# -*- coding: utf-8 -*-
from django.contrib import admin
from django.db.models.loading import get_models, get_app
from django.contrib.admin.sites import AlreadyRegistered


for model in get_models(get_app('usuarios')):
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass
