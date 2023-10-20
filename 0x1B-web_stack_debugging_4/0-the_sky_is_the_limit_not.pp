# Change the number of nginx traffic from default to a higher number

exec { 'increase-limit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path => '/usr/local/bin/:/bin',
}

# restart nginx
exec {'restart-nginx':
  command => '/usr/sbin/service nginx restart',
}
