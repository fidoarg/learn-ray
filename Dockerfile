FROM rayproject/ray:2.9.2.038e3b-py310-aarch64

WORKDIR /home/ray

COPY ./main.py main.py

COPY ./requirements.txt requirements.txt

RUN pip install -r ./requirements.txt