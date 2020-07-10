In the Lecture_Docker directory as the location of a docker-compose.yml file, execute:

**Lecture_Docker$** _docker-compose up --abort-on-container-exit --exit-code-from tests_

The images of simple-app, and the tests will be built and run. 
The log will be saved in _Lecture_Docker/reports_ as nicely readable (idented) .json file
