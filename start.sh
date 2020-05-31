#!/bin/bash
app="docker.imiona"
docker build -t ${app} .
docker run -d -p 5000:5000 ${app}

