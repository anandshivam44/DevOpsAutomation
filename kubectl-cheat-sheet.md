## Kubernetes Cheat Sheet  

#### Create a yaml file to get started
```bash
kubectl run redis --image=redis --dry-run=client -o yaml > redis-definition.yaml
kubectl get events -o wide
kebectl get po -o wide
```
#### Create pod and expose with service of type ClusterIp
```bash
kubectl run httpd --image=httpd:alpine --port=80 --expose
```

#### ReplicaSets commands
```bash
kubectl get replicasets
kubectl get rs
kubectl describe replicasets new-replica-set
kubectl explain replicaset | grep VERSION
kubectl explain rs
kubectl edit replicaset new-replica-set
kubectl scale rs new-replica-set --replicas=2
```
#### Kubernetes get everything
```bash
kubectl get all
```
#### kubectl Usage Conventions
[kubectl Usage Conventions](https://kubernetes.io/docs/reference/kubectl/conventions/)

#### Create an NGINX Pod
```bash
kubectl run nginx --image=nginx
```

#### Generate POD Manifest YAML file (-o yaml). Don't create it(--dry-run)
```bash
kubectl run nginx --image=nginx --dry-run=client -o yaml
```

#### Create a deployment
```bash
kubectl create deployment --image=nginx nginx
```
#### deployment commands
```bash
kubectl expose deployment nginx --port=80
kubectl edit deployment nginx
kubectl scale deployment nginx --replicas=5
kubectl set image deployment nginx nginx=nginx:1.18
```

#### Generate Deployment YAML file 
```bash
kubectl create deployment --image=nginx nginx --dry-run=client -o yaml
kubectl create deployment --image=nginx nginx --dry-run=client -o yaml > nginx-deployment.yaml
```


#### Generate Deployment YAML file with --replicas 
```bash
kubectl create deployment --image=nginx nginx --replicas=4 --dry-run=client -o yaml > nginx-deployment.yaml
```
#### Create nodeport service template
```bash
kubectl create service  nodeport webapp-service --tcp=8080:8080 --node-port=30080 --dry-run=client -o yaml
```

#### Service commands
```bash
kubectl get service
kubectl get svc
kubectl describe service kubernetes
kubectl expose pod redis --port=6379 --name redis-service --dry-run=client -o yaml #Create a Service named redis-service of type ClusterIP to expose pod redis on port 6379
kubectl create service  nodeport webapp-service --tcp=8080:8080 --node-port=30080 --dry-run=client -o yaml > service.yml
kubectl create service clusterip redis --tcp=6379:6379 --dry-run=client -o yaml #Create a Service named redis-service of type ClusterIP to expose pod redis on port 6379
kubectl expose pod nginx --type=NodePort --port=80 --name=nginx-service --dry-run=client -o yaml #Create a Service named nginx of type NodePort to expose pod nginx's port 80 on port 30080 on the nodes
```

#### namespace commands
```bash
kubectl get ns
kubectl get namespace
kubectl get namespaces
kubectl create namespace dev
kubectl create namespace dev --dry-run=client -o yaml
kubectl get po --namespace=dev
kubectl get po -n=dev
kubectl  config set-context $(kubectl config current-context) --namespace=dev # permanently change current namespace context
kubectl get pods --all-namespaces
kubectl get po -A
```
#### work with files
```bash
kubectl create -f nginx.yml
kubectl replace -f nginx.yml
kubectl replace --force -f nginx.yml
kubectl delete -f nginx.yml

# Apply command is declarative approach, it will figure out itself how to do
kubectl apply -f nginx.yml
```
#### add label
```bash
kubectl run redis -l tier=db --image=redis:alpine
```

#### filtering and using selectors
```bash
kubectl get po --selector app=App1
kubectl get po --selector env=prod,bu=finance,tier=frontend
kubectl get po --selector app=App1 --no-headers | wc -l
```
#### Taints and Toleration
Nodes can be taint and pods can be tolerant  
taint effect can be NoSchedule | PreferNoSchedule | NoExecute
```bash
kubectl taint nodes node-name key=value:taint-effect
kubectl taint nodes node-name app=blue:NoSchedule
kubectl describe node kubermaster | grep Taint

# Remove Taint from node
kubectl taint nodes controlplane key=value:NoSchedule-
```

#### Node selector
```bash
kubectl label nodes node-name key=value
```
#### DaemonSets
```bash
kubectl get daemonsets
kubectl describe daemonsets monitoring-daemon
```
#### Static Pods
```bash
ps -aux | grep kube # then look for --client 
path /etc/kubernetes/manifests
```
#### Basic monitoring
```bash
kubectl top node
kubectl top pod
kubectl top pod --sort-by='cpu' --no-headers | tail -1
```
#### Basic Logging
```bash
kubectl logs pod-name
kubectl logs pod-name -c container-name
```
#### Rollout and Rollback
```bash
kubectl rollout status deployment/myapp
kubectl rollout history deployment/myapp
kubectl rollout undo deployment/myapp
kubectl get replicasets
```
#### ConfigMaps
```bash
kubectl get configmap
kubectl get cm
kubectl describe configmaps db-config
kubectl create configmap webapp-config-map --from-literal=APP_COLOR=darkblue
kubectl create configmap webapp-config-map --from-literal=APP_COLOR=darkblue --from-literal=APP_BACKGROUND=pink 
```
#### ConfigMaps
```bash
echo -n "mysql" | base64
echo -n "bx1cZax=" | base64 --decode

kubectl get secrets
kubectl describe secrets
kubectl describe secrets db-config
kubectl create secret generic webapp-config-map --from-literal=APP_COLOR=darkblue
kubectl create secret generic webapp-config-map --from-literal=APP_COLOR=darkblue --from-literal=APP_BACKGROUND=pink 
```
#### execute commands
```bash
kubectl exec -it pod-name -- cat /log/app.log
```
#### Os Upgrades % Cluster Upgrade
```bash
kubectl drain node01 --ignore-daemonsets #take out all pods in node so that node can go down for maintainance
kubectl uncordon node01 #bring back node
kubectl cordon node01 #do not create new pods 

# Upgrade cluster
kubectl cordon controlplane
apt-get update
kubeadm upgrade plan 
https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/
apt-mark unhold kubeadm &&  apt-get update && apt-get install -y kubeadm=1.26.1-00 &&  apt-mark hold kubeadm
kubeadm upgrade node # only for worker nodes
kubeadm upgrade plan
kubeadm upgrade apply v1.26.0
apt search kubelet
apt upgrade kubelet=1.26.1-00
k get no
systemctl daemon-reload
systemctl restart kubelet
k get no
kubectl uncordon controlplane
```

#### Backup
```bash
kubectl get all --all-namespaces -0 yaml > all-deploy-services.yaml

etcdctl --version
kubectl get po -n=kube-system
kubectl describe pod etcd-controlplane -n kube-system


export ETCDCTL_API=3 # when working with etcdctl
etcdctl snapshot save -h



kubectl -n kube-system describe pod etcd-controlplane | grep '\--listen-client-urls'      --listen-client-urls=https://127.0.0.1:2379,https://192.50.67.3:2379


ETCDCTL_API=3 etcdctl --endpoints=https://[127.0.0.1]:2379 \
--cacert=/etc/kubernetes/pki/etcd/ca.crt \
--cert=/etc/kubernetes/pki/etcd/server.crt \
--key=/etc/kubernetes/pki/etcd/server.key \
snapshot save /opt/snapshot-pre-boot.db



ETCDCTL_API=3 etcdctl  --data-dir /var/lib/etcd-from-backup \
snapshot restore /opt/snapshot-pre-boot.db

watch "crictl ps | grep etcd"




etcdctl snapshot restore -h


```


#### cluster config
```bash
kubectl config get-clusters
kubectl config use-context cluster1    
```

#### Certificate Signing Request CSR
```bash
kubectl get csr
kubectl certificate approve <username>  
kubectl get csr <username> -o yaml
kubectl certificate deny <username>
kubectl delete csr agent-smith
```
#### Config, user , permissions
```bash
kubectl config current-context --kubeconfig my-kube-config
kubectl config --kubeconfig=/root/my-kube-config use-context research
kubectl config --kubeconfig=/root/my-kube-config current-context
```

#### Authorization
```bash
kubectl get roles
kubectl get rolebindings
kubectl describe role developer
kubectl describe rolebindings <developer-role-binding>

# check if you have access
kubectl auth can-i create deployment
kubectl auth can-i delete nodes

kubectl auth can-i create deployment --as dev-user
kubectl auth can-i delete nodes --as dev-user

kubectl create role developer --namespace=default --verb=list,create,delete --resource=pods
kubectl create rolebinding dev-user-binding --namespace=default --role=developer --user=dev-user

kubectl create role developer --namespace=default --verb=list,create,delete --resource=pods --dry-run=client -o yaml > lab1.yml
kubectl create rolebinding dev-user-binding --namespace=default --role=developer --user=dev-user  --dry-run=client -o yaml > lab2.yml

kubectl  edit role developer -n blue

```

#### Namespace
```bash
kubectl api-resources --namespaced=true
kubectl api-resources --namespaced=false
```

#### Service Account
```bash
kubectl create serviceaccount dashboard-sa
kubectl get serviceaccount 
kubectl describe serviceaccount dashboard-sa
kubectl describe secret dashboard-sa-token
```



