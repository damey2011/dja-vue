#!/usr/bin/env bash
docker run -it alpine:3.6 sh -c "apk add --no-cache libffi-dev build-base py2-pip python2-dev && pip install cffi"