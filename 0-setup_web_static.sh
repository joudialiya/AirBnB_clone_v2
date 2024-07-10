#!/usr/bin/env bash
# This script will setup the server for deployment

sudo apt-get update
sudo apt-get -y install nginx

DATA_FOLDER="/data"
WEB_STATIC="${DATA_FOLDER}/web_static"
WEB_STATIC_SHARED="${WEB_STATIC}/shared"
WEB_STATIC_RELEASES="${WEB_STATIC}/releases"
WEB_STATIC_TEST="${WEB_STATIC_RELEASES}/test"
WEB_STATIC_CURRENT="${WEB_STATIC}/current"

mkdir -p ${WEB_STATIC_TEST}
mkdir -p ${WEB_STATIC_SHARED}

# we create th dummy file
echo "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > "${WEB_STATIC_TEST}/index.html"
# create symbolic link
ln -sf ${WEB_STATIC_TEST} ${WEB_STATIC_CURRENT}

chown -hR ubuntu:ubuntu ${DATA_FOLDER}

echo "
server {
        listen 80;
        listen [::]:80;

        server_name _;

        location / {
            try_files \$uri \$uri/ =404;
        }
        location /hbnb_static {
            alias ${WEB_STATIC_CURRENT};
            index index.html;
        }
}" > "/etc/nginx/sites-available/default"

service nginx restart