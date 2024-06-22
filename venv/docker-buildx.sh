#!/bin/sh
set -e

mkdir -p ~/.docker/cli-plugins/
cd ~/.docker/cli-plugins/
wget https://github.com/docker/buildx/releases/download/v0.11.1/buildx-v0.11.1.linux-amd64
mv buildx-v0.11.1.linux-amd64 docker-buildx
chmod 755 docker-buildx