FROM linuxserver/transmission

ENV PORT 5000
EXPOSE 5000

COPY requirements.txt /tmp/
# Copy in webhook listener script
COPY webhook.py /
COPY s6-action.sh /

RUN \
    echo "**** install packages ****" \
        && apk add --no-cache \
        python3 \
        \
    && \
    echo "**** python requirements ****" \
        && if [ ! -e /usr/bin/python ]; then ln -sf python3 /usr/bin/python ; fi \
        && python3 -m ensurepip \
        && rm -r /usr/lib/python*/ensurepip \
        && pip3 install --no-cache --upgrade pip -r /tmp/requirements.txt \
        && if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi \
        \
    && \
    echo "*** chmod ***" \
        && chmod +x /s6-action.sh

CMD ["python3", "webhook.py"]