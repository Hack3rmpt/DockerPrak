FROM openjdk:alpine

LABEL version="1.0.21"

WORKDIR /the/workdir/path

COPY . /the/workdir/path/

RUN javac game.java

CMD [ "java", "game" ]