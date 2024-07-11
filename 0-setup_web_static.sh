#!/usr/bin/env bash

apt-get -y update
apt-get -y install nginx
ufw allow 'Nginx HTTP'
echo 'Hello World!' > /var/www/html/index.nginx-debian.html
sed -i '/listen 80 default_server;/a rewrite ^/redirect_me https://github.com/MohamedAlaga permanent;' /etc/nginx/sites-available/default
echo "Ceci n'est pas une page" > /usr/share/nginx/html/custom_404.html
sed -i '/server_name _;/a error_page 404 /custom_404.html;\nlocation = /custom_404.html {\nroot /usr/share/nginx/html;\ninternal;\n}' /etc/nginx/sites-available/default
sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default
service nginx start
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "hello World! HBNB clone" >> /data/web_static/releases/test/index.html
ln -sf /data/web_static/current /data/web_static/releases/test/
sudo chown -R ubuntu:ubuntu /data/
sed -i '/rewrite ^/redirect_me https://github.com/MohamedAlaga permanent;/a location /hbnb_static/{ alias /data/web_static/current/;}' /etc/nginx/sites-available/default
service nginx restart
