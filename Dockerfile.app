# we use a bearstech image!
FROM bearstech/python-dev:3

# we create a user for our app and install selenium
ARG uid=1001
RUN useradd python --uid ${uid} --shell /bin/bash --home /home/python \
    && pip3 install selenium

WORKDIR /home/python


# copy our project
COPY ./app.py /home/python/
COPY ./test_selenium.py /home/python/
COPY ./html /home/python/html

# use our user
USER python

# run our application
CMD ["python", "app.py"]
