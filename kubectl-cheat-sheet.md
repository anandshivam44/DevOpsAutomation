## Kubernetes Cheat Sheet  

#### Create a yaml file to get started
```bash
kubectl run redis --image=redis --dry-run=client -o yaml > redis-definition.yaml
```
