FROM python:3.9
RUN apt update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
        git \
        libtbb-dev && \
    rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/CDLUC3/ezid-client-tools
RUN chmod +x /ezid-client-tools/ezid3.py
RUN ln -s /ezid-client-tools/ezid3.py /usr/local/bin/ezid3.py
WORKDIR /workdir
ENTRYPOINT [ "ezid3.py" ]