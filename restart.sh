docker-compose down
docker image rm hackathon-2022-11-04-web
PORT=8080
docker build ./App
docker-compose up -d
