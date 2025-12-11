docker build -t autn/adventofcode ./docker
docker run -it --rm -v "$PWD":/usr/src/myapp -w /usr/src/myapp autn/adventofcode pip freeze > "$PWD/docker/requirements_installed.txt"