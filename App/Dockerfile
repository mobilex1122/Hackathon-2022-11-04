FROM python
WORKDIR /app
COPY . .
# Install requirements
RUN ["python", "-m", "pip", "install", "-r", "./requirements.txt"]
WORKDIR /app

# Setup Env
ARG PORT
ENV FLASK_DEBUG=False
ENV FLASK_PORT=$PORT

# Expose ports
EXPOSE ${FLASK_PORT}

# Run the application
CMD ["python3", "./main.py"]
