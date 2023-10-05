#!/usr/bin/env bash
# A script to prepare the web servers for airbnb deployment
sudo apt-get update
sudo apt-get install -y nginx

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

echo "Holberton School" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu /data/
chgrp -R ubuntu /data/

printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current/;
	index index.html
    }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-enabled/default

sudo service nginx restart
