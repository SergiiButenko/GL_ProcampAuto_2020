FROM maven:3.6.3-jdk-8-slim

RUN mkdir /simple-app-tests
WORKDIR /simple-app-tests

COPY ./src ./src
COPY pom.xml ./pom.xml

RUN mvn package -DskipTests

ENTRYPOINT ["mvn", "surefire-report:report"]

