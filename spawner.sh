#!/bin/bash
cd /home/late/dev/heater
until python daemon.py; do
    echo "Heater daemon crashed with exit code $?.  Respawning..." >&2
    sleep 1
done
