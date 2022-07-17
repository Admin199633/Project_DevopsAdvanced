# Project_Devops

description :
1. Docker images for the consumer and producer applications.
2. Helm charts for deploying consumer and producer applications.
3. CI Pipeline - I will use him to clone, build and push the application’s docker images.
4. CD Pipeline -  I will use him to build push and deploy the application’s helm charts.
5. I used  Helm for deploy RabbitMQ
![Untitled-1-Recovered copy](https://user-images.githubusercontent.com/108216254/179386944-dc91dfa4-c336-4a63-afdb-e49b47aae777.jpg)





# Creata DND(docker in docker):
![dockerindocker](https://user-images.githubusercontent.com/108216254/179387298-45570e48-1316-4866-83da-06395cab62a5.jpg)


# RabbitMQ
###  RabbitMQ - an application that is able to store data in a queue fashion allowing us tohave the ability to maintain a queue of messages

install RabbitMQ:

```
helm install rabbitmq --set auth.username=user,auth.password=Lior12345,auth.erlangCookie=secretcookie,metrics.enabled=true,persistence.enabled=true bitnami/rabbitmq
```

![rabbitmq](https://user-images.githubusercontent.com/108216254/179387498-ac152ce3-906e-42de-8c3e-3a2cc3687f8b.jpg)

expose rabbitmq to port 5672:
```
start /min python ./expose-RabbitMQ.py
```
![expose rabbitmq](https://user-images.githubusercontent.com/108216254/179387798-901c46bc-9e94-41c7-b952-98470aa3519a.jpg)


# Build Docker image and push
```
docker build -t devops:%BUILD_NUMBER% ./producer
docker build -t devops:%BUILD_NUMBER% ./consumer
docker tag devops:%BUILD_NUMBER% photop/devops:%BUILD_NUMBER%
docker push photop/devops:%BUILD_NUMBER%
```
![images](https://user-images.githubusercontent.com/108216254/179389062-99d86878-8c90-43fc-86e7-594fa069e2b7.jpg)

