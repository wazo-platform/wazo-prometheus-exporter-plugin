#!/bin/bash

hostname="${1:localhost}"

METRICS=$(cat <<- EOV
    /api/amid/1.0/metrics
    /api/asterisk/metrics
    /api/auth/0.1/metrics
    /api/call-logd/1.0/metrics
    /api/calld/1.0/metrics
    /api/chatd/1.0/metrics
    /api/confd/1.1/metrics
    /api/dird/0.1/metrics
    /api/nginx/metrics
    /api/node/metrics
    /api/phoned/0.1/metrics
    /api/postgresql/metrics
    /api/rabbitmq/metrics
    /api/sysconfd/metrics
    /api/sysconfd/metrics
    /api/webhookd/1.0/metrics
EOV
)

result=0
for metric in $METRICS; do
    url="https://${hostname}${metric}"
    for i in {1..60}; do
        if curl -skf -o /dev/null "$url"; then
            echo "${url} OK"
            break
        else
            echo "${url} FAIL"
            if [ "${i}" -eq "10" ]; then
                result=1
                break
            fi
            sleep 5
        fi
    done
done
exit ${result}
