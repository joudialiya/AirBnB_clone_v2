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

cat /etc/nginx/sites-available/default | grep "location /hbnb_static"

if [[ echo "$?" -ne 0 ]]; then
	sed -i "/server_name/a \\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t\tindex index.html;\n\t}" "/etc/nginx/sites-available/default"
fi

service nginx restart


