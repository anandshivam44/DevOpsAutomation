## Important and Useful Linux Commands for Daily Life and Interviews

__________________
#### pushd popd dir
pushd and popd both are a combination of commands that are used to navigate file-system very similar to cd command. Their special feature is that they can store your paths in a stack
```
pushd my-folder-1-path # change my directory to folder 1
pushd my-folder-2-path # change my directory to folder 2
pushd my-folder-3-path # change my directory to folder 3
# You are currently in folder 3 and folder-2 and folder-1 are also in stack
# Now you can go back to folder-2 using
popd
# Now you can go back again to folder-1 using
popd
```
`pushd` & `popd` are used when you are navigating FS and want to go back to your previous folder quickly.
__________________
#### cron cronjob crontab
___
#### free
___
#### ps -a
___
#### top
___
#### anacron
___
#### Ctrl +r
___
#### Ctrl + Left Arrow Ctrl + Right Arrow
___
#### chmod
___
#### chown
___
#### top
___
#### uptime
___
#### cal
It gets calender of the current month in terminal. Use it to to save time.
```
cal
```
```
    January 2022
Su Mo Tu We Th Fr Sa
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30 31
```
![Calendar Output](./images/cal-command.png)
___
#### push a command to background using &
___
#### bash vs shell
___
#### sleep
___
#### ssh
ssh -i "public key.pem" ec2-user@3.51.32.0 if you ssh very frequently and do not want to use the -i command then follow https://github.com/anandshivam44/DevOpsAutomation/blob/main/GenerateKeysAndSSH.md
___
#### fg bg with Ctrl z
___
#### jobs
___
#### ping
___
#### kill
___
#### du -sh /var/log/* du -sh /var/log/
___
#### grep 
grep -nr 'anand.shivam44' anandshivam44.github.io/ to find a particular word in complete folder
___
#### free
___
#### pkill
___
#### sed
 sed 's/unix/linux/g' geekfile.txt
___
#### soft link ln -s
#### hard link ln
___
#### rsync
___
###### What is dev/null?
To understand easy, assume `dev/null` is a Black Hole. You can direct output of any commant is scripts to dev/null. It is very much used in scripts where you want to suppress errors. For example

___
#### what is 2>&1
___
#### curl ifconfig.me
```
curl ifconfig.me
```
It is used to get your current IPv4
![IPv4](./images/curl_ifconfig.PNG)
___
#### ifconfig
___
#### netstat
Listening Port: netstat -ntlp
___
.bash_profile
.bashrc
___
#### word count: wc
___
#### $env
___
#### vmstat
___
#### htop
___
#### tree .
The `tree` command is used to get directory structure in the form of a tree. Paste output in your Github Readme to make your project directory easy to understand for a second person. 
![tree](./images/tree-command.png)
___
#### unmask
___
sudo netstat -tulpn | grep LISTEN
___
#### dmesg
Boot time logs: dmesg
___
When you are working on servers there are no IDEs and you have to use `vim` or `nano` to edit a file. But if you want to just empty a file then the fastest way is
```
echo "" > file.txt
```
using vim and nano in this situation could be tidious.
___
What is the shebang line in shell scripting?
___
input.txt | python3 my-program.py > output.txt
___
base64
___
I want to read all input to the command from file1 direct all output to file2 and error to file 3, how can I achieve this command <file1 1>file2 2>file3
awk
___
#### df
df -i to get available node number
___
sticky bits in linux permission
___
###### What is return code in bash/shell scripts?
Every Bash script has a return code. The code could be as follows:-
0 for success  
1 if no matches were f   &
2 if the script throwed an error while executing  

However there are 256 return codes ranging from 1 - 255