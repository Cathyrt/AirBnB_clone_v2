# Script that sets up  web servers for the deployment 
exec { '/usr/bin/env apt -y update' : }
-> package { 'nginx':
  ensure => installed,
}
-> file { '/data/web_static/releases/test':
  ensure => 'directory'
}
-> file { '/data/web_static/shared':
  ensure => 'directory'
}
-> file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => "<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    <p>Holberton School</p>
  </body>
</html>"
}
-> file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test'
}
-> file { '/data':
  ensure  => 'directory',
}  
-> exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}
-> file { '/etc/nginx/sites-available/default':
  content => "server {\n\tlisten 80 default_server;\n\tlisten [::]:80 default_server;\n\n\troot /var/www/html;\n\tindex index.html index.htm index.nginx-debian.html;\n\n\tserver_name _;\n\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n}",
  require => Package['nginx'],
  notify  => Service['nginx'],
}
-> service { 'nginx':
  ensure => running,
}
