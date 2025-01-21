FROM python:3.9.6-alpine3.14

WORKDIR /app

COPY . .

# Install only allowed dependencies
RUN apk add --no-cache gcc libffi-dev musl-dev ffmpeg && pip install --no-cache-dir -r requirements.txt

CMD gunicorn app:app & python3 main.py
