# Fixed wrong extension in wp-settings.php

exec{'fix-wp':
  provider => 'shell',
  command  => 'sed -i "s/\.phpp/\.php/g" /var/www/html/wp-settings.php',
}
