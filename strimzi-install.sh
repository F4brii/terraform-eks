#!/bin/bash
kubectl apply -f https://strimzi.io/install/latest?namespace=default -n default

kubectl apply -f https://strimzi.io/examples/latest/kafka/kafka-ephemeral.yaml -n default