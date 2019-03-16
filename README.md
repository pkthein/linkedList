** installing docker-compose **

** did not need to install docker for aws c9 **

sudo curl -L "https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m)"  -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

docker-compose --version

** running the sawtooth docker shell **

docker exec -it sawtooth-shell-default bash

# fun_with_sorting
# linkedList
