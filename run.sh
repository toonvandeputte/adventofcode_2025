# docker run -it --rm -v "$PWD/site-packages":/usr/local/lib/python3.14/site-packages "pip install --no-cache-dir -r requirements.txt"

docker run -it --rm -v "$PWD":/usr/src/myapp -w /usr/src/myapp autn/adventofcode pip freeze > "$PWD/docker/requirements_installed.txt"

docker run -it --rm -v "/Users":"/Users" -v "$PWD":/usr/src/myapp -w /usr/src/myapp autn/adventofcode python $@