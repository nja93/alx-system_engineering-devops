#this script configures a brand new Ubuntu machine to the requirements below


#automate the task of creating a custom HTTP header response, but with Puppet
#The name of the custom HTTP header must be X-Served-By
#value of the custom HTTP header must be the hostname of the server Nginx is running on

# This block of code updates package information
exec { 'apt-update':
  command => '/usr/bin/apt-get -y update',
  path    => ['/usr/bin', '/bin'],
}

# This block installs Nginx package
package { 'nginx':
  ensure => installed,
}

# This block of code creates a basic HTML file
file { '/var/www/html/index.html':
  content => 'Hello World!',
}

# This code configure Nginx to add the custom HTTP header
file_line { 'add custom header':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "\tadd_header X-Served-By ${hostname};",
  after  => 'server_name _;',
}

# This code ensures Nginx is running
service { 'nginx':
  ensure => running,
}
