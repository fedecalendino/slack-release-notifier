FROM python:3.10-slim AS build-env
ADD . /app
WORKDIR /app

RUN pip install --target=/app -r requirements.txt

FROM gcr.io/distroless/python3-debian10
COPY --from=build-env /app /app
WORKDIR /app
ENV PYTHONPATH /app
CMD ["/app/main.py"]