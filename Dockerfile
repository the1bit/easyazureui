# EasyUI - Azure
# Python3
FROM python:3

# Labels
LABEL version="19.08.01" \
    maintainer="the1bithu@gmail.com" \
    environment="azure" \
    web="Flask" \
    app="python3" \
    technology="restapi"



# Copy easyui to /src
COPY /easyui /easyui 


WORKDIR /easyui

## Install dependencies
RUN pip3 install -r requirements.txt --no-cache-dir --user

# Listener port
EXPOSE 5555

ENTRYPOINT [ "python3", "./runserver.py"]
