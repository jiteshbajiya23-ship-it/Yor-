FROM python:3.11
WORKDIR /app
COPY . .
RUN chmod +x start.sh
CMD ["bash", "start.sh"]
