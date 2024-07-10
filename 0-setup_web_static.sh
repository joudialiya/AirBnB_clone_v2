#!/usr/bin/env bash
# This script will setup the server for deployment

sudo apt-get update
sudo apt-get -y install nginx

mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared/

# we create th dummy file
echo "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > "/data/web_static/releases/test/index.html"
# create symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -hR ubuntu:ubuntu /data

echo "
server {
        listen 80;
        listen [::]:80;

        server_name _;

        location / {
            try_files \$uri \$uri/ =404;
        }
        location /hbnb_static {
            alias /data/web_static/current;
            index index.html;
        }
}" > "/etc/nginx/sites-available/default"

service nginx restart