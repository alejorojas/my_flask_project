#!/usr/bin/env bash

docker-compose down
docker-compose up -d --scale web=3
docker logs -f python_nginx_web_1
