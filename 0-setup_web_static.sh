#!/usr/bin/env bash
#this bash script installs, configures and sets up  web servers for the deployment of web_static .
sudo apt update -y
sudo apt install nginx -y
sudo ufw allow 'Nginx HTTP'

# Create necessary directories if they don't exist
sudo mkdir -p /data/web_static/releases/test 
sudo mkdir -p /data/web_static/shared 

# Create a fake HTML file for testing
echo "<html><head></head><body>Holberton School</body></html>" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Set ownership to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# Restart Nginx to apply changes
sudo service nginx restart
