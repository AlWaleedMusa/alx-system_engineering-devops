# puppet settings for nginx

# install Nginx
package { 'nginx':
    ensure => installed,
}

# configure Nginx
file_line { 'install':
  ensure => 'present',
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.github.com/alwaleedmusa permanent;',
}

# make sure its running
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
