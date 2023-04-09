FROM ubuntu:22.04
WORKDIR app

ENV PYUSB_DEBUG=debug

RUN apt-get update
RUN apt-get upgrade
RUN apt-get install python3-pip -y
RUN apt-get install libusb-1.0.0-dev -y

# COPY libopenusb_1.1.16-0_amd64.deb libopenusb_1.1.16-0_amd64.deb

# RUN apt install ./libopenusb_1.1.16-0_amd64.deb -y

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pip install pipenv

RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy
ENV PATH="/.venv/bin:$PATH"


COPY . .

EXPOSE 8000

RUN pipenv run python3 core/manage.py makemigrations
RUN pipenv run python3 core/manage.py migrate

CMD [ "pipenv", "run", "python3", "core/manage.py", "runserver", "0.0.0.0:8000", "--noreload"]    
