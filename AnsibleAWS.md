## Quick Start Ansible for AWS
### Starter Ansible template  for AWS
Create a host and a managed-node

Then install ansible inside host. Below command is for Amazon linux2.
```bash
sudo amazon-linux-extras install ansible2
```
Verify ansible is installed
```bash
ansible --version
```
Copy contents of pem file to host (Assuming you created managed-node on AWS and you downloaded your .pem file with which you can SSH to your managed-node). Read the contents of .pem file and copy-paste to a new file `key.pem`. You can use vim or nano editor to paste contents.
You need to reduce the permission of your key file.
```bash
 chmod 400 key.pem 
```
Now in your ansible host machine. Add key file to ssh-agent.
```bash
ssh-agent bash
cp key.pem ~/.ssh/
chmod 400 ~/.ssh/key.pem
ssh-add ~/.ssh/key.pem
```
Create inventory file `inventory.txt`. Inventory file is used to store hosts meta-data. Here we are explicityly creating a host file but the default host file is located in `/etc/ansible/hosts`  
  
  
Create  host file
```bash
touch inventory.txt
```
Inside the file paste
```
myservers ansible_host=54.242.242.100 ansible_connection=ssh ansible_user=ec2-user
```
Try to ping the host and check if you have a successful connection
```bash
 ansible myservers -m ping -i inventory.txt
```
<!-- Manual Authentication. Press yes when prompted. -->

make sure you are in the same session in which you added bash key, if not you may want to do again `ssh-agent bash` & `ssh-add ~/.ssh/key.pem`

<!-- Optional
```bash
export ANSIBLE_HOST_KEY_CHECKING=False
``` -->

To disble host checking every time. Set host_key_checking = False in `/etc/ansible/ansible.cfg`
```bash
sudo vi /etc/ansible/ansible.cfg
```
Inside the `ansible.cfg` file. Uncomment the line below.
```
host_key_checking = False # uncomment this line
```
Now start writing playbook. Create a file `install-ngix.yaml`. Here is an example playbook. You can create a playbook of your own.
```yaml
- name: Setup nginx on server list
  hosts: myserver
  become: True

  tasks:

    - name: install latest version of nginx
      command: amazon-linux-extras install nginx1.12=latest -y

    - name: start nginx service
      service:
          name: nginx
          state: started

    - name: enable nginx service
      service:
          name: nginx
          enabled: yes

    - name: Get nginx version
      command: nginx -v

    - name: Get status nginx service
      command: systemctl status nginx 
```

<!-- ```bash
sudo vi /etc/ansible/hosts
``` -->
<!-- add your hosts to the file
```
[myservers]
35.175.171.151 -->
<!-- ``` -->
Now run the playbook
```bash
ansible-playbook install-nginx.yaml -vv
```
Ansible will start a nginx server in your managed-node.
If Ansible successfully deployed nginx and you are still cannot open your nginx site on your managed-mode, try to check your security groups, network settings and firewall settings.
