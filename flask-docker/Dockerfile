FROM alpine:latest


RUN apk update && apk add --no-cache python3-dev py3-pip libffi-dev build-base && pip3 install --upgrade pip

WORKDIR /OWASP-top-10-CTF-USW-Project

COPY . /OWASP-top-10-CTF-USW-Project

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["app.py"]

