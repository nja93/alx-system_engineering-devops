# give holberton user access

exec {'holberton':
  command => 'sed -i 's/holberton/#holberton/' /etc/security/limits.conf',
  path    => [ '/usr/bin', '/bin/', '/usr/sbin' ],
}
