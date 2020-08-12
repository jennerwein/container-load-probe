#!/bin/sh

NAME=container-load-probe

# Aufräumen
docker container stop ${NAME}
docker container rm ${NAME}

# Zuerst das Image bauen
docker rmi jennerwein/${NAME}:latest
docker build -t jennerwein/${NAME}:latest .

# Starten des Images
docker run -p 8080:8080 --name ${NAME} --restart=always -d jennerwein/${NAME}

