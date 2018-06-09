#!/bin/bash

cd  "$(dirname $0)"

for i in {1..20}
do
  ./1-check_connections.py
  sleep 5
done
