#!/usr/bin/env python3
# Copyright 2023-2026 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

import yaml
from setuptools import setup

with open('wazo/plugin.yml') as file:
    metadata = yaml.load(file, Loader=yaml.SafeLoader)

# Other services ship their own metrics plugin since Wazo 26.11
fastapi_entry_point_path = (
    'metrics = wazo_prometheus_exporter.plugins.fastapi.metric.plugin:Plugin',
)

fastapi_entry_point_key = [
    'wazo_sysconfd.plugins',
]

fastapi_entry_points = {
    key: fastapi_entry_point_path for key in fastapi_entry_point_key
}

setup(
    version=metadata['version'],
    description=metadata['display_name'],
    author=metadata['author'],
    url=metadata['homepage'],
    entry_points=fastapi_entry_points,
)
