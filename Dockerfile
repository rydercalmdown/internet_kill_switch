FROM debian:buster
WORKDIR /code
RUN apt-get update && apt-get install -y dnsmasq
RUN cat /etc/dnsmasq.conf
