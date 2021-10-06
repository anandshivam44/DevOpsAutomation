## SSH from one ec2 to another ec2. Generate key and SSH from one VM to another VM.
#### Step 1
Generate key in your client machine/laptop
```bash
ssh-keygen -t rsa -b 4096 -C [USERNAME_OF_YOUR_CHOICE]
```
#### Step 2
##### Step 2: Linux & Mac
Add the key to your ssh-agent. Doing this will make life easier. You will not have to provide a private key during ssh in the terminal
```bash
eval $(ssh-agent -s)
```

```bash
ssh-add ~/.ssh/id_rsa
```
##### Step 2: Windows
```Powershell
# By default the ssh-agent service is disabled. Allow it to be manually started for the next step to work.
# Make sure you're running as an Administrator.
Get-Service ssh-agent | Set-Service -StartupType Manual

# Start the service
Start-Service ssh-agent

# This should return a status of Running
Get-Service ssh-agent

# Now load your key files into ssh-agent
ssh-add ~\.ssh\id_rsa
```

#### Step 3
Now copy the contents of the file `id_rsa.pub` to the clipboard.
```bash
cat ~/.ssh/id_rsa.pub
```
#### Step 4
In the remote server in which you want to SSH/setup SSH.
It might sound funny/confusing, but yes you need to access this system (i.e. login with SSH or user-password) and modify some files. Without this, you cannot proceed further.

```bash
echo "PASTE CONTENTS OF id_rsa.pub FILE HERE" >> ~/.ssh/authorized_keys
```
#### Step 5
Now everything is ready
You can now ssh from your client to a remote machine with just one command. Replace `username` with your remote machine username and replace your IP address. 
```bash
ssh [USERNAME]@[IP]
```
