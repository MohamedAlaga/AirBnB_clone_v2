#!/usr/bin/env bash
#add alias to /hbnb_static

apt-get -y update
apt-get -y install nginx
ufw allow 'Nginx HTTP'
service nginx start
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "hello World! HBNB clone" >> /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sed -i '/listen 80 default_server;/a \\tlocation /hbnb_static/ { \n\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
service nginx restart
