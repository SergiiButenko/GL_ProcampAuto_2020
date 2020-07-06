- Build the image:

**Lecture_Docker$** _docker build -t simple-app-pytest ._

- Run the image with -v key,
mapping a folder on your host to the /app/test/logs/ folder in the image
where logs pytest logs after each the pytest session run are stored:

**Lecture_Docker$** _docker run -v </absolute path to folder on your host>:/app/test/logs/ simple-app-pytest_