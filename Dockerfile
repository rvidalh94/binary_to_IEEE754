FROM python:3.9.7-alpine3.14

ADD conversion.py /

WORKDIR /binary_to_IEEE754/binary_to_IEEE754

CMD ["python3", "conversion.py"]
