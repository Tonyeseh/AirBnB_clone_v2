#!/usr/bin/env bash
# installs nginx if not already installed
# creates some folders
# and configures nginx to server that folder

apt-get update
apt-get -y install ngnix

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

echo "server {
	listen 80 default_server;
	listen [::]:80 default_server;

	root /var/www/html;
	index index.html index.htm index.nginx-debian.html;

	location /hbnb_static {
		alias /data/web_static/current/;
		index index.html index.htm;
	}
	
	location /redirect_me {
		return 301 https:/www/youtube.com/watch?v=QH2-TGUlwu4;
	}

	error_page 404 /404_not_found.html;
	location /404 {
		root /var/www/html;
		internal;
	}
}" | sudo tee /etc/nginx/sites-available/default

sudo service nginx restart
