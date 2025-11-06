# wazo-prometheus-exporter-plugin

Adds `/metrics` to the wazo-auth service as well as Asterisk and Nginx

## Installation

```sh
wazo-plugind-cli -c "install git https://github.com/wazo-platform/wazo-prometheus-exporter-plugin"
```

## Metrics endpoints

> [!WARNING]
> Internal metrics will be available on **port 6387**. This port must be closed
> by a firewall to avoid exposing the metrics to the public.

- asterisk `/asterisk/metrics`
- nginx `/nginx/metrics`
- rabbitmq `/rabbitmq/metrics`
- wazo-agentd `/agentd/1.0/metrics`
- wazo-amid `/amid/1.0/metrics`
- wazo-auth `/auth/0.1/metrics`
- wazo-call-logd `/call-logd/1.0/metrics`
- wazo-calld `/calld/1.0/metrics`
- wazo-chatd `/chatd/1.0/metrics`
- wazo-confd `/confd/1.1/metrics`
- wazo-dird `/dird/0.1/metrics`
- wazo-phoned `/phoned/0.1/metrics`
- wazo-sysconfd `/sysconfd/metrics`
- wazo-webhookd `/webhookd/1.0/metrics`

## Prometheus scrape config

On the Prometheus instance server, the relevant endpoints must be configured in
the Prometheus configuration file. The `targets` field should include the Wazo
server's IP address. You may need to update this field to reflect the correct IP
address.

```yaml
scrape_configs:
  ...
  - job_name: wazo-agentd
    scheme: http
    metrics_path: /agentd/1.0/metrics
    static_configs:
      - targets: ['localhost:6387']
        labels:
          framework: 'flask'
          service: 'wazo-agentd'

  - job_name: wazo-amid
    scheme: http
    metrics_path: /amid/1.0/metrics
    static_configs:
      - targets: ['localhost:6387']
        labels:
          framework: 'flask'
          service: 'wazo-amid'

  - job_name: wazo-auth
    scheme: http
    metrics_path: /auth/0.1/metrics
    static_configs:
      - targets: ['localhost:6387']
        labels:
          framework: 'flask'
          service: 'wazo-auth'

  - job_name: wazo-call-logd
    scheme: http
    metrics_path: /call-logd/1.0/metrics
    static_configs:
      - targets: ['localhost:6387']
        labels:
          framework: 'flask'
          service: 'wazo-call-logd'

  - job_name: wazo-calld
    scheme: http
    metrics_path: /calld/1.0/metrics
    static_configs:
      - targets: ['localhost:6387']
        labels:
          framework: 'flask'
          service: 'wazo-calld'

  - job_name: wazo-chatd
    scheme: http
    metrics_path: /chatd/1.0/metrics
    static_configs:
      - targets: ['localhost:6387']
        labels:
          framework: 'flask'
          service: 'wazo-chatd'

  - job_name: wazo-confd
    scheme: http
    metrics_path: /confd/1.1/metrics
    static_configs:
      - targets: ['localhost:6387']
        labels:
          framework: 'flask'
          service: 'wazo-confd'

  - job_name: wazo-dird
    scheme: http
    metrics_path: /dird/0.1/metrics
    static_configs:
      - targets: ['localhost:6387']
        labels:
          framework: 'flask'
          service: 'wazo-dird'

  - job_name: wazo-phoned
    scheme: http
    metrics_path: /phoned/0.1/metrics
    static_configs:
      - targets: ['localhost:6387']
        labels:
          framework: 'flask'
          service: 'wazo-phoned'

  - job_name: wazo-sysconfd
    scheme: http
    metrics_path: /sysconfd/metrics
    static_configs:
      - targets: ['localhost:6387']
        labels:
          framework: 'fastapi'
          service: 'wazo-sysconfd'

  - job_name: wazo-webhookd
    scheme: http
    metrics_path: /webhookd/1.0/metrics
    static_configs:
      - targets: ['localhost:6387']
        labels:
          framework: 'flask'
          service: 'wazo-webhookd'

  - job_name: 'asterisk'
    metrics_path: /asterisk/metrics
    scheme: http
    static_configs:
      - targets: ['localhost:6387']

  - job_name: nginx
    scheme: http
    metrics_path: /nginx/metrics
    static_configs:
      - targets: ['localhost:6387']

  - job_name: rabbitmq
    scheme: http
    metrics_path: /rabbitmq/metrics
    static_configs:
      - targets: ['localhost:6387']

  - job_name: postgresql
    scheme: http
    metrics_path: /postgresql/metrics
    static_configs:
      - targets: ['localhost:6387']

  - job_name: node
    scheme: http
    metrics_path: /node/metrics
    static_configs:
      - targets: ['localhost:6387']

  - job_name: process
    scheme: http
    metrics_path: /process/metrics
    static_configs:
      - targets: ['localhost:6387']
```
