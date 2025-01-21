FROM python:3.9

RUN pip install pandas

###Creates app directory-slash-folder within docker image
WORKDIR /app

COPY pipeline.py pipeline.py

ENTRYPOINT [ "python", "pipeline.py" ]