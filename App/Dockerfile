FROM python
WORKDIR /app
COPY . .
# Install requirements
RUN ["python", "-m", "pip", "install", "-r", "./requirements.txt"]
WORKDIR /app

# Setup Env
ENV FLASK_DEBUG=False
ENV FLASK_PORT=8080

# Expose ports
EXPOSE ${FLASK_PORT}

# Run the application
CMD ["python3", "./main.py"]
