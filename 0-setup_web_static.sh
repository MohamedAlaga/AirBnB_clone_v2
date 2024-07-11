#!/usr/bin/env bash

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
ln -sf /data/web_static/current /data/web_static/releases/test/
sudo chown -R ubuntu:ubuntu /data/
sed -i '/rewrite ^/redirect_me https://github.com/MohamedAlaga permanent;/a \nlocation /hbnb_static/ { \nalias /data/web_static/current/;\n}' /etc/nginx/sites-available/default
service nginx restart
