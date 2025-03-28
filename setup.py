#!/usr/bin/env python3
# Copyright 2023-2025 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

import yaml

from setuptools import find_packages
from setuptools import setup

with open('wazo/plugin.yml') as file:
    metadata = yaml.load(file)

flask_entry_point_path = 'metrics = wazo_prometheus_exporter.plugins.flask.metric.plugin:Plugin'
fastapi_entry_point_path = 'metrics = wazo_prometheus_exporter.plugins.fastapi.metric.plugin:Plugin',

flask_entry_point_key = [
    'wazo_agentd.plugins',
    'wazo_amid.plugins',
    'wazo_auth.http',
    'wazo_call_logd.plugins',
    'wazo_calld.plugins',
    'wazo_dird.views',
    'wazo_chatd.plugins',
    'wazo_confd.plugins',
    'wazo_phoned.plugins',
    'wazo_webhookd.plugins',
]
fastapi_entry_point_key = [
    'wazo_sysconfd.plugins',
]

flask_entry_points = {key: flask_entry_point_path for key in flask_entry_point_key}
fastapi_entry_points = {key: fastapi_entry_point_path for key in fastapi_entry_point_key}

setup(
    name=metadata['name'],
    version=metadata['version'],
    description=metadata['display_name'],
    author=metadata['author'],
    url=metadata['homepage'],

    packages=find_packages(),
    include_package_data=True,
    package_data={
        'wazo_prometheus_exporter.plugins.flask.metric': ['api.yml'],
    },
    entry_points=dict(
        **fastapi_entry_points,
        **flask_entry_points,
    ),
)
