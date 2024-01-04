#!/usr/bin/env bash
# A bash script that sets up my web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
content="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"
echo -e "$content" | sudo tee /data/web_static/releases/test/index.html > /dev/null
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

if ! grep -q "location /hbnb_static {" /etc/nginx/sites-available/default; then
	sudo sed -i '/^[^#]*location \/ {/ { :a; N; /}/!ba; s/}/&\n\n        location \/hbnb_static {\n                alias \/data\/web_static\/current\/;\n        }/; }' /etc/nginx/sites-available/default
fi

sudo service nginx restart
