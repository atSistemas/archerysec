# -*- coding: utf-8 -*-
#                    _
#     /\            | |
#    /  \   _ __ ___| |__   ___ _ __ _   _
#   / /\ \ | '__/ __| '_ \ / _ \ '__| | | |
#  / ____ \| | | (__| | | |  __/ |  | |_| |
# /_/    \_\_|  \___|_| |_|\___|_|   \__, |
#                                     __/ |
#                                    |___/
# Copyright (C) 2017 Anand Tiwari
#
# Email:   anandtiwarics@gmail.com
# Twitter: @anandtiwarics
#
# This file is part of ArcherySec Project.

from django.urls import include, path
from projects import views

app_name = 'projects'

urlpatterns = [
    path('create/',
        views.create,
        name='create'),
    path('create_form/',
        views.create_form,
        name='create_form'),
    path('',
        views.projects,
        name='projects'),
    path('project_edit/',
        views.project_edit,
        name='project_edit'),
]
