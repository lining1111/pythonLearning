FROM ubuntu:latest
LABEL authors="lining"
COPY /etc/apt/sources.list /etc/apt
COPY ./app /app/
EXPOSE 10001
VOLUME ["/app/log/"]
CMD ["executable","param1","param2"]