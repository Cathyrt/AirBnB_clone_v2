# Install and configures web servers for the deployment of web_static.

exec { 'apt-update':
  command => '/usr/bin/apt-get update',
  path    => '/usr/bin:/usr/local/bin:/bin',
} ->

package { 'nginx':
  ensure => installed,
} ->

file { '/data/web_static/releases/test':
  ensure => 'directory',
} ->

file { '/data/web_static/shared':
  ensure => 'directory',
} ->

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => "<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    <p>Holberton School</p>
  </body>
</html>",
} ->

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
} ->

exec { 'set-data-ownership':
  command => '/bin/chown -R ubuntu:ubuntu /data',
  path    => '/usr/bin:/usr/local/bin:/bin',
} ->

file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => "server {
                listen 80 default_server;
                listen [::]:80 default_server;

                root /var/www/html;
                index index.html index.htm index.nginx-debian.html;

                server_name _;

                location /hbnb_static/ {
                  alias /data/web_static/current/;
                }
              }",
  require => Package['nginx'],
  notify  => Service['nginx'],
} ->

service { 'nginx':
  ensure => 'running',
}
