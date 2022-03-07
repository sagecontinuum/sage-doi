FROM python:3.9
RUN apt update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
        git \
        libtbb-dev && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /workdir
COPY ezid_schema/schema-cli.py schema-cli.py
RUN chmod +x schema-cli.py
COPY ezid_schema/requirements.txt requirements.txt
RUN pip install -r requirements.txt
ENTRYPOINT [ "./schema-cli.py" ]