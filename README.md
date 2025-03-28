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
* wazo-call-logd `api/call-logd/1.0/metrics`
* wazo-calld `/api/calld/1.0/metrics`
* wazo-chatd `/api/chatd/1.0/metrics`
* wazo-confd `/api/confd/1.1/metrics`
* wazo-dird `/api/dird/0.1/metrics`
* wazo-phoned `:9499/0.1/metrics`
* wazo-sysconfd `/api/sysconfd/metrics`
* wazo-webhookd `/api/webhookd/1.0/metrics`

## Prometheus scrape config

On the prometheus instance server, those endpoints need to be configured in the prometheus config:

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
  - job_name: wazo-calld
    scheme: https
    tls_config:
      insecure_skip_verify: true
    metrics_path: /api/calld/1.0/metrics
    static_configs:
      - targets: ['localhost:443']
  - job_name: wazo-chatd
    scheme: https
    tls_config:
      insecure_skip_verify: true
    metrics_path: /api/chatd/1.0/metrics
    static_configs:
      - targets: ['localhost:443']
  - job_name: wazo-sysconfd
    scheme: https
    tls_config:
      insecure_skip_verify: true
    metrics_path: /api/sysconfd/metrics
    static_configs:
      - targets: ['localhost:443']
  - job_name: wazo-dird
    scheme: https
    tls_config:
      insecure_skip_verify: true
    metrics_path: /api/dird/0.1/metrics
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
```
