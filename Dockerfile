FROM python:3.9.7-alpine3.14

WORKDIR /binary_to_IEEE754
COPY . .

CMD ["conversion.py"]
ENTRYPOINT ["python3"]