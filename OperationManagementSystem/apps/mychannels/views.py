# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, reverse

app_name = 'mychannels'


def config_deploy_record(request):
    return render(request, 'mychannels/config_deploy_record.html', {})
