#!/bin/sh

# If you want to push it manually

TAG=200812
NAME=container-load-probe

docker login

docker push jennerwein/${NAME}:latest 


