# Copyright 2023-2025 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from starlette_exporter import PrometheusMiddleware, handle_openmetrics


class Plugin:
    def load(self, dependencies: dict):
        api = dependencies['api']

        api.add_middleware(PrometheusMiddleware)
        api.add_route('/metrics', handle_openmetrics)
