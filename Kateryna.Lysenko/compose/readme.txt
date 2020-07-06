# Build simple-app
# run from simple-app dir.
docker build -t simple-app .

# Building simple-app-tests
# run from simple-app-tests dir.
docker build -t simple-app-tests .

# Running docker-compose from compose dir
# mount reports to ./report dir of the host system 
docker-compose up --abort-on-container-exit --exit-code-from simple-app-tests

# running above, but using Dockerfile`s instead of images
docker-compose -f docker-compose-with-build.yml up --abort-on-container-exit --exit-code-from simple-app-tests