# Automates the 500 server error fix
# change from ".phpp" to ".php"

exec { 'fix-wordpress':
    command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    path    => '/usr/local/bin/:/bin/'
}
