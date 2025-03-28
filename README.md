# wazo-prometheus-exporter-plugin

Adds `/metrics` to the wazo-auth service as well as Asterisk and Nginx

## Installation

```sh
wazo-plugind-cli -c "install git https://github.com/wazo-platform/wazo-prometheus-exporter-plugin"
```

## Metrics endpoints

* asterisk `/api/asterisk/metrics`
* nginx `/api/nginx/metrics`
* rabbitmq `/api/rabbitmq/metrics`
* wazo-agentd `/api/agentd/1.0/metrics`
* wazo-amid `/api/amid/1.0/metrics`
* wazo-auth `/api/auth/0.1/metrics`
* wazo-calld `/api/calld/1.0/metrics`
* wazo-chatd `/api/chatd/1.0/metrics`
* wazo-confd `/api/confd/1.1/metrics`
* wazo-dird `/api/dird/0.1/metrics`
* wazo-sysconfd `/api/sysconfd/metrics`

## Prometheus scrape config

On the Prometheus instance server, the relevant endpoints must be configured in
the Prometheus configuration file. The `targets` field should include the Wazo
server's IP address. You may need to update this field to reflect the correct IP
address.


``````yaml
scrape_configs:
  ...
  - job_name: wazo-auth
    scheme: https
    tls_config:
      insecure_skip_verify: true
    metrics_path: /api/auth/0.1/metrics
    static_configs:
      - targets: ['localhost:443']
        labels:
          framework: 'flask'
          service: 'wazo-auth'

  - job_name: wazo-calld
    scheme: https
    tls_config:
      insecure_skip_verify: true
    metrics_path: /api/calld/1.0/metrics
    static_configs:
      - targets: ['localhost:443']
        labels:
          framework: 'flask'
          service: 'wazo-calld'

  - job_name: wazo-chatd
    scheme: https
    tls_config:
      insecure_skip_verify: true
    metrics_path: /api/chatd/1.0/metrics
    static_configs:
      - targets: ['localhost:443']
        labels:
          framework: 'flask'
          service: 'wazo-chatd'

  - job_name: wazo-dird
    scheme: https
    tls_config:
      insecure_skip_verify: true
    metrics_path: /api/dird/0.1/metrics
    static_configs:
      - targets: ['localhost:443']
        labels:
          framework: 'flask'
          service: 'wazo-dird'

  - job_name: wazo-sysconfd
    scheme: https
    tls_config:
      insecure_skip_verify: true
    metrics_path: /api/sysconfd/metrics
    static_configs:
      - targets: ['localhost:443']
        labels:
          framework: 'fastapi'
          service: 'wazo-sysconfd'

  - job_name: 'asterisk'
    metrics_path: /api/asterisk/metrics
    scheme: https
    tls_config:
      insecure_skip_verify: true
    static_configs:
      - targets: ['localhost:443']

  - job_name: nginx
    scheme: https
    tls_config:
      insecure_skip_verify: true
    metrics_path: /api/nginx/metrics
    static_configs:
      - targets: ['localhost:443']

  - job_name: rabbitmq
    scheme: https
    tls_config:
      insecure_skip_verify: true
    metrics_path: /api/rabbitmq/metrics
    static_configs:
      - targets: ['localhost:443']

  - job_name: postgresql
    scheme: https
    tls_config:
      insecure_skip_verify: true
    metrics_path: /api/postgresql/metrics
    static_configs:
      - targets: ['localhost:443']

  - job_name: node
    scheme: https
    tls_config:
      insecure_skip_verify: true
    metrics_path: /api/node/metrics
    static_configs:
      - targets: ['localhost:443']

  - job_name: process
    scheme: https
    tls_config:
      insecure_skip_verify: true
    metrics_path: /api/process/metrics
    static_configs:
      - targets: ['localhost:443']
```
