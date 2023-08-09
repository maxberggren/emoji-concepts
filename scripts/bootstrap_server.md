    ##################################################################################
    #  _                 _       _                                                   #
    # | |__   ___   ___ | |_ ___| |_ _ __ __ _ _ __    ___  ___ _ ____   _____ _ __  #
    # | '_ \ / _ \ / _ \| __/ __| __| '__/ _` | '_ \  / __|/ _ \ '__\ \ / / _ \ '__| #
    # | |_) | (_) | (_) | |_\__ \ |_| | | (_| | |_) | \__ \  __/ |   \ V /  __/ |    #
    # |_.__/ \___/ \___/ \__|___/\__|_|  \__,_| .__/  |___/\___|_|    \_/ \___|_|    #
    #                                         |_|                                    #
    ##################################################################################

### First send all files to prod machine
`bash scripts/deploy_app.sh`

### Go to machine manually
`ssh root@$SERVER_ADDR`

### When on machine, run everything following block by block to verify that it works
`source .env`

### Usual suspects
```bash
yes | apt update -y
yes | apt install -y make libpq-dev build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
yes | apt install postgresql-client
yes | apt install sqlite3
```

### Pyenv
```bash
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.bashrc
exec "$SHELL"
pyenv install 3.8.11
```

### Poetry for dependency management
```bash
curl -sSL https://install.python-poetry.org | python3 -
echo 'export PATH="/root/.local/bin:$PATH"' >> ~/.bashrc
export PATH="/root/.local/bin:$PATH"
```

### Supervisord that will keep the Python app alive
```bash
yes | apt install python3-pip
yes | pip3 install supervisor
mkdir /logs/
mkdir  /etc/supervisor/
touch  /etc/supervisor/supervisord.conf
echo "; Sample supervisor config file.
[unix_http_server]
file=/tmp/supervisor.sock   ; the path to the socket file

[supervisord]
logfile=/tmp/supervisord.log ; main log file; default $CWD/supervisord.log
logfile_maxbytes=50MB        ; max main logfile bytes b4 rotation; default 50MB
logfile_backups=10           ; # of main logfile backups; 0 means none, default 10
loglevel=info                ; log level; default info; others: debug,warn,trace
pidfile=/tmp/supervisord.pid ; supervisord pidfile; default supervisord.pid
nodaemon=false               ; start in foreground if true; default false
minfds=1024                  ; min. avail startup file descriptors; default 1024
minprocs=200                 ; min. avail process descriptors

[rpcinterface:supervisor]
supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface

[supervisorctl]
serverurl=unix:///tmp/supervisor.sock ; use a unix:// URL for a unix socket

[include]
files=conf.d/*.conf" > /etc/supervisor/supervisord.conf
mkdir /etc/supervisor/conf.d/
supervisord
```

### Logonscreen just because it's fun
```bash
sudo chmod -x /etc/update-motd.d/*
yes | sudo apt install inxi screenfetch ansiweather
yes | sudo apt install figlet toilet
echo '#!/bin/sh
echo "Welcome to $SERVER_NAME server"
figlet $SERVER_NAME
/usr/bin/screenfetch -n
echo
echo "SYSTEM DISK USAGE"
export TERM=xterm; inxi -D' > /etc/update-motd.d/01-custom
sudo chmod +x /etc/update-motd.d/01-custom
```

### Nginx will be our frontline handling requests
```bash
yes | apt install nginx
sudo ufw allow 'Nginx HTTP'
```

### Certbot so we are ready to go https later
```bash
apt install snapd
sudo snap install core; sudo snap refresh core
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
```

### Set the hostname
`echo $SERVER_NAME > /etc/hostname`

### Install virtualenv with dependencies
`poetry install`

### Now, from local mashine – run:
```bash
bash scripts/install_tailwind.sh
bash scripts/deploy_supervisor.sh
bash scripts/deploy_nginx.sh
```