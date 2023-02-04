## Kubernetes Cluster using kubeadm

##### --> 
Check connectivity between master and slave
```bash
ping IP
```
Disable swap
```bash
sudo swapoff -a  
cat /proc/meminfo | grep 'SwapTotal'
free -h
```
prepare
```bash
sudo apt get update
sudo apt install -y net-tools vim git curl wget netcat
```


sudo which nft >/dev/null && echo nftables is enabled in this system || echo ufw is enabled in this system

##### --> 
On Control Panel aka master node allow [relavent ports](https://kubernetes.io/docs/reference/networking/ports-and-protocols/)
```bash
sudo which nft >/dev/null && echo nftables is enabled in this system || echo ufw is enabled in this system

nc 127.0.0.1 6443
sudo netstat -tulpn | grep LISTEN
nc -zv  127.0.0.1 22
nc -zv  127.0.0.1 6443
netstat -lntu
ss -lntu

sudo apt install ufw
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw allow 6443
sudo ufw allow 2379:2380/tcp
sudo ufw allow 30000:32768/tcp
sudo ufw allow 10250
sudo ufw allow 10259
sudo ufw allow 10257
sudo ufw enable
sudo ufw status
```
  
On Worker node(s) [relavent ports](https://kubernetes.io/docs/reference/networking/ports-and-protocols/)
```bash
netstat -lntu
ss -lntu

sudo apt install ufw
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw allow 10250
sudo ufw allow 30000:32767/tcp
sudo ufw enable
sudo ufw status
```
##### --> 
Install docker from the given link [Install Docker](https://docs.docker.com/engine/install/)

##### --> 
For Docker you need to install [cri-dockerd](https://github.com/Mirantis/cri-dockerd)
```bash
git clone https://github.com/Mirantis/cri-dockerd.git
```

To install cri-dockerd you need to install [Go programming](https://go.dev/doc/install) Language
Download and install Go specific to your CPU architecture
After installing go
```bash
echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.profile 
source ~/.profile 
go version
```
Compile and install `cri-dockerd`
##### --> 
[Forwarding IPv4 and letting iptables see bridged traffic](https://kubernetes.io/docs/setup/production-environment/container-runtimes/#forwarding-ipv4-and-letting-iptables-see-bridged-traffic)
##### --> 
[Installing kubeadm, kubelet and kubectl](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/#installing-kubeadm-kubelet-and-kubectl)

##### --> 
After installation
kubeadm init
```bash
sudo kubeadm init --pod-network-cidr=192.168.0.0/16 --control-plane-endpoint=172.31.0.47 --cri-socket=unix:///var/run/cri-dockerd.sock
```
* `--pod-network-cidr=192.168.0.0/16` because Calico supports 192.168.0.0/16 and I can use Acalico  

Install Calico to provide both networking and network policy for self-managed on-premises deployments.
* `--cri-socket=unix:///var/run/cri-dockerd.sock` pass cri socket for cri-dockerd
* `--control-plane-endpoint=172.31.0.47` private Ip here
```bash
kubectl get pods -A
```
##### --> 
After kubeadm init follow the output given by the command
##### --> 
Setup Calico  
[Install Calico networking and network policy for on-premises deployments](https://projectcalico.docs.tigera.io/getting-started/kubernetes/self-managed-onprem/onpremises)
directly jump to Install Calico Manifest Tab and follow "Install Calico with Kubernetes API datastore, 50 nodes or less"
```bash
kubectl get pods -A
```
```bash
kubectl get pods -A --watch
kubectl get namespaces
kubectl get all -n kube-system
```
##### --> 
On the Worker Node
* Install docker and `docker-cri`
* Install kubeadm, kubelet and kubectl
```bash
sudo kubeadm join IP:6443 --token TOKEN --discovery-token-ca-cert-hash CERT --cri-socket=unix:///var/run/cri-dockerd.sock
```
Dont forget to pass `--cri-socket=unix:///var/run/cri-dockerd.sock`
##### --> More References

[kubeadm join after link is expired](https://stackoverflow.com/questions/40009831/cant-find-kubeadm-token-after-initializing-master)


