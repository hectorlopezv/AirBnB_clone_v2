#!/usr/bin/env bash
#prepare your web servers
apt install nginx -y
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Holberton Schol" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i   '/server_name _;/a location /hbnb_static { alias /data/web_static/current/; \n\tautoindex off; }' /etc/nginx/sites-available/default
sudo nginx -s reload



