#!/usr/bin/env python3

import yaml

from setuptools import find_packages
from setuptools import setup

with open('wazo/plugin.yml') as file:
    metadata = yaml.load(file)

flask_entry_point_path = 'metrics = wazo_prometheus_exporter.plugins.flask.metric.plugin:Plugin'
flask_entry_point_key = [
    'wazo_auth.http',
    'wazo_dird.views',
    'wazo_chatd.plugins',
]
flask_entry_points = {key: flask_entry_point_path for key in flask_entry_point_key}

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
    entry_points=flask_entry_points,
)
