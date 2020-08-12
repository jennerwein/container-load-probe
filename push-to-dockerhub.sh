#!/bin/sh

# If you want to push it manually

TAG=200811
NAME=container-load-probe

docker login

docker push jennerwein/${NAME}:latest 
docker push jennerwein/${NAME}:${TAG}


