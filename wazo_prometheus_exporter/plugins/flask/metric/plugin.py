# Copyright 2023-2025 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

import logging

from prometheus_flask_exporter import RESTfulPrometheusMetrics

logger = logging.getLogger(__name__)


class Plugin:
    def load(self, dependencies):
        api = dependencies['api']

        path = f'{api.prefix}/metrics'
        logger.debug('Registering Prometheus metrics endpoint at %s', path)
        RESTfulPrometheusMetrics(api.app, api, path=path, group_by='endpoint')
