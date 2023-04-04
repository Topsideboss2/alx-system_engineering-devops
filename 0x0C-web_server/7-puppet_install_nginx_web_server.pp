# Configuration Management
# Web server
# Install an Nginx Server using a puppet manifest

exec {'install':
  provider => shell,
  command  => 'sudo apt-get -y update ; sudo apt-get -y install nginx ; echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html ; sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/github.com\/topsideboss2 permanent;/" /etc/nginx/sites-available/default ; sudo service nginx start',
}
