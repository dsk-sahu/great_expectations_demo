FROM brunneis/python
RUN apt update
RUN apt install -y python3-pip
RUN pip install great_expectations