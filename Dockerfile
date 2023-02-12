FROM golang:alpine

WORKDIR /app

ENV PYTHONUNBUFFERED=1

RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

RUN apk add git make gcc musl-dev libc-dev


# Domain enumeration
RUN go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
RUN go install -v github.com/tomnomnom/assetfinder@latest
RUN go install -v github.com/OWASP/Amass/v3/...@master
RUN git clone https://github.com/blechschmidt/massdns.git && cd massdns && make
RUN pip install Sublist3r
RUN pip install fierce


# RUN go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest


RUN export PATH=$PATH:/app/massdns/bin