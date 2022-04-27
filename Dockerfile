FROM alpine:latest


RUN apk update && apk add --no-cache python3-dev py3-pip libffi-dev build-base && pip3 install --upgrade pip

WORKDIR /OWASP-top-10-CTF-USW-Project

COPY . /OWASP-top-10-CTF-USW-Project

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["app.py"]


# Vulnerable and outdated components
FROM plone:5.2.4
#environment variable to create a plone site
ENV SITE=plone
WORKDIR /plone/instance
RUN echo FLAG{test} >> flag.txt