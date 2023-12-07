# wazo-prometheus-exporter-plugin

Adds `/metrics` to the wazo-auth service as well as Asterisk and Nginx

## Installation

```sh
wazo-plugind-cli -c "install git https://github.com/wazo-platform/wazo-prometheus-exporter-plugin"
```

## Metrics endpoints

* asterisk `/api/asterisk/metrics`
* nginx `/api/nginx/metrics`
* wazo-auth `/api/auth/0.1/metrics`
* wazo-calld `/api/calld/1.0/metrics`
* wazo-chatd `/api/chatd/1.0/metrics`
* wazo-dird `/api/dird/0.1/metrics`
* wazo-sysconfd `/api/sysconfd/metrics`
