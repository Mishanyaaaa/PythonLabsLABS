# LAB4

1. Docker працює правильно:
   - sudo docker -v
   - sudo docker -h
   - sudo docker run docker/whalesay cowsay Docker is fun 
     
2. Перенаправив вивід в my_work.log:
   - sudo docker -v > my_work.log
   - sudo docker -h >> my_work.log 
   - sudo docker run docker/whalesay cowsay Docker is fun >> my_work.log
3. Завантажив базовий імедж з репозиторію
   - "sudo docker pull python:3.8-slim"
   - "sudo docker images"
   - "sudo docker inspect python:3.8-slim"
   - Створив файл з іменем Dockerfile
   - Замінив посилання на власний Git репозиторій
4. Створив власний репозиторій на Docker Hub

5. Виконав білд (build) Docker імеджа та завантажив його до репозиторію:
   - sudo docker build -t mishaaanya/lab4:django .
   - sudo docker images
   - sudo docker push mishaaanya/lab4:monitoring
6. Запустив веб-сайт:
    - sudo docker run -it --rm -p 8000:8000 mishaaanya/lab4:django
7. Домашня робота:
   - створив Dockerfile.site
   - Виконав білд імеджа:
       - sudo docker build -f Dockerfile.site -t mishaaanya/lab4:monitoring .
       - sudo docker images
       - sudo docker push mishaaanya/lab4:monitoring
   - Записав логи: 
        - sudo docker run -it --rm -p 8000:8000 mishaaanya/lab4:django
        - sudo docker run -it --rm --net=host -v $(pwd)/server.log:/app/server.log mishaaanya/lab4:monitoring
8. Посилання:
    - [репозиторій](https://hub.docker.com/repository/docker/mishaaanya/lab4)
    - [джанго](https://hub.docker.com/layers/131316738/mishaaanya/lab4/django/images/sha256-4d7f4a96c18db35c77f0e64afdd2a9d11cbe016c9df2139da43d62ee2186fa70?context=explore)
    - [моніторинг](https://hub.docker.com/layers/131321338/mishaaanya/lab4/monitoring/images/sha256-4571c768a55b97d0c40a23367b899807f1107fab9d7b8f8d075e5264fee637e6?context=explore)
