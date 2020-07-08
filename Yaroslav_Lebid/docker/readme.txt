#JSON report on test execution written to: ../docker/srs/.report.json linked to host

# to create image with simpleapp running on port 5002 (run from '../docker/simpleapp' folder)
docker build -t simpleapp .

# run simple-app container
docker run simpleapp

# to create image with test (run from '../docker/tests' folder)
#(changed test to wait from 2 minutes to 10 seconds for quick check)
docker build -t tests .

# run container from image and share volume on my folder structure
# YES, I'm on Windows :) please use your env folder for -v
docker run --link simpleapp -v C:\\cygwin64\\home\\Yas\\GL_ProcampAuto_2020\\Yaroslav_Lebid\\docker\\src:/src tests


=============================================================
# run docker-compose w/o images from '../docker' folder
docker-compose -f docker-compose.yml up --abort-on-container-exit --exit-code-from tests