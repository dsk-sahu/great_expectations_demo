FROM brunneis/python
RUN apt update -y
RUN apt install -y python3-pip
RUN pip install great_expectations
RUN mkdir /tmp/GE
WORKDIR /tmp/GE
COPY . /tmp/GE
RUN ls -lrt
RUN yes | great_expectations init
RUN python createDataSource.py
RUN python createExpectations.py
RUN python createCheckpoint.py
RUN ls -lrt /great_expectations/uncommitted/data_docs/local_site
