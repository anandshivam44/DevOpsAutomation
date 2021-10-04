## SSH from one ec2 to another ec2. Generate key and SSH from one VM to another VM.
Generate key in your client machine/laptop
```bash
ssh-keygen
```
Add the key to your ssh-agent. Doing this will make life easier. You will not have to provide private key during ssh in the terminal
```bash
eval $(ssh-agent -s)
```

```bash
ssh-add ~/.ssh/id_rsa
```
Now copy the contents of the file `id_rsa.pub` to clipboard.
```bash
cat ~/.ssh/id_rsa.pub
```
In the remote server in which you want to SSH/setup SSH.
It might sound funny/confusing, but yes you need to access this system (i.e. login with SSH or user-password) and modify some files. Withot this you cannot proceed further.

```bash
echo "PASTE CONTENTS OF id_rsa.pub FILE HERE" >> ~/.ssh/authorized_keys'
```
Now everything is ready
You can now ssh from your client to remote machine with just one command. Replace `username` with your own remote machine username and replace your IP address. 
```bash
ssh username@34.140.120.136
```
