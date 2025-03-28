# Copyright 2023-2025 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

import re
import logging

from prometheus_flask_exporter import PrometheusMetrics

logger = logging.getLogger(__name__)

TOKEN_URL_RE = re.compile(r"/token/([a-zA-Z0-9-]+)")
ANONYMIZED_TOKEN = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'


def path(req):
    matches = TOKEN_URL_RE.search(req.path)
    if matches:
        token = matches.group(1)
        return req.path.replace(token, ANONYMIZED_TOKEN)

    return req.path


class Plugin:
    def load(self, dependencies):
        api = dependencies['api']

        path = f'{api.prefix}/metrics'
        logger.debug('Registering Prometheus metrics endpoint at %s', path)
        self.metrics = PrometheusMetrics(api.app, path=path, group_by=path)
