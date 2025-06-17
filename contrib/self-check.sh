#!/bin/bash

hostname="${1:-localhost}"

METRICS=$(cat <<- EOV
    /amid/1.0/metrics
    /asterisk/metrics
    /auth/0.1/metrics
    /call-logd/1.0/metrics
    /calld/1.0/metrics
    /chatd/1.0/metrics
    /confd/1.1/metrics
    /dird/0.1/metrics
    /nginx/metrics
    /node/metrics
    /phoned/0.1/metrics
    /postgresql/metrics
    /rabbitmq/metrics
    /sysconfd/metrics
    /sysconfd/metrics
    /webhookd/1.0/metrics
EOV
)

result=0
for metric in $METRICS; do
    url="http://${hostname}:6387${metric}"
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
