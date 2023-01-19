wget -o jenkins.war $url
sudo cp /usr/share/java/jenkins.war /usr/share/java/jenkins.war.backup
sudo cp ./jenkins.war /usr/share/java/jenkins.war
( sleep 3; sudo systemctl restart jenkins; sleep 2) &
