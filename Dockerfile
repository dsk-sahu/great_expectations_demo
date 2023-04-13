FROM brunneis/python
RUN apt update -y
RUN apt install -y python3-pip
RUN pip install great_expectations
RUN mkdir /tmp/GE
WORKDIR /tmp/GE
COPY . /tmp/GE
