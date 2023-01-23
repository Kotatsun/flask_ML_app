#!/bin/sh

### container
IMAGE=flask/torch:latest
CONTAINER_NAME=flask_app_train
FLASK_PORT_MAP=5000
MOUNT=${PWD}
MOUNT_MAP=/home/flask_app

docker run -it -d --rm \
--ipc=host \
--name ${CONTAINER_NAME} \
--hostname ${CONTAINER_NAME} \
-v ${MOUNT}:${MOUNT_MAP} \
-e gid=`id -g` \
-w ${MOUNT_MAP} \
${IMAGE}

docker exec ${CONTAINER_NAME} bash -c "python mnist_train.py"