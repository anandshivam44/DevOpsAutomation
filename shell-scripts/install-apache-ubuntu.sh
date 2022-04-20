echo "#!/bin/bash
sudo apt update -y
sudo apt install -y apache2
sudo ufw enable
sudo ufw allow 'Apache'
sudo ufw allow ssh
sudo echo "<h1>This is a test server</h1>" > /var/www/html/index.html
sudo systemctl restart apache2
