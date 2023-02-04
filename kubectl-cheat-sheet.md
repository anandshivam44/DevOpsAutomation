## Kubernetes Cheat Sheet  

#### Create a yaml file to get started
```bash
kubectl run redis --image=redis --dry-run=client -o yaml > redis-definition.yaml
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
