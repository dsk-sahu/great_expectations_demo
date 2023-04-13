FROM brunneis/python
RUN apt update -y
RUN apt install -y python3-pip
RUN pip install great_expectations
RUN mkdir /tmp/GE
WORKDIR /tmp/GE
COPY . /tmp/GE
RUN ls -lrt
RUN great_expectations init -y
RUN createDataSource.py
RUN createExpectations.py
RUN createCheckpoint.py
RUN ls -lrt /great_expectations/uncommitted/data_docs/local_site
