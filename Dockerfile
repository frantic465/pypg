FROM ubuntu:latest

RUN \
  apt-get update && \
  apt-get install -y python python-dev python-pip python-virtualenv && \
  rm -rf /var/lib/apt/lists/*

CMD ["python", "tests/tests.py"]

