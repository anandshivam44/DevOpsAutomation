## Kubernetes Cheat Sheet  

#### Create a yaml file to get started
```bash
kubectl run redis --image=redis --dry-run=client -o yaml > redis-definition.yaml
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
