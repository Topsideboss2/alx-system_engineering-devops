# Fixed wrong extension in wp-settings.php

exec('fix-wp':
  command => 'sed -i "s/\.php/\.php7/g" /var/www/html/wp-settings.php',
  path    => ['/bin', '/usr/bin'],
)
