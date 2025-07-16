# n8n Kubernetes Deployment

This folder contains Kubernetes manifests for deploying n8n with PostgreSQL on Kubernetes clusters.

## 🚀 Quick Start

### Using the Deployment Script (Recommended)

```bash
# Make scripts executable
chmod +x deploy.sh cleanup.sh

# Deploy n8n
./deploy.sh
```

### Manual Deployment

1. **Create namespace**:
   ```bash
   kubectl apply -f namespace.yaml
   ```

2. **Create secrets and configmaps**:
   ```bash
   kubectl apply -f postgres-secret.yaml
   kubectl apply -f postgres-configmap.yaml
   ```

3. **Create persistent volume claims**:
   ```bash
   kubectl apply -f n8n-claim0-persistentvolumeclaim.yaml
   kubectl apply -f postgres-claim0-persistentvolumeclaim.yaml
   ```

4. **Deploy PostgreSQL**:
   ```bash
   kubectl apply -f postgres-deployment.yaml
   kubectl apply -f postgres-service.yaml
   ```

5. **Deploy n8n**:
   ```bash
   kubectl apply -f n8n-deployment.yaml
   kubectl apply -f n8n-service.yaml
   ```

## 🔧 Configuration

### Before Deployment

⚠️ **IMPORTANT**: Update the credentials in `postgres-secret.yaml` before deploying:

```yaml
stringData:
  POSTGRES_USER: your_db_user
  POSTGRES_PASSWORD: your_secure_password
  POSTGRES_NON_ROOT_USER: your_n8n_user
  POSTGRES_NON_ROOT_PASSWORD: your_n8n_password
```

### Storage Configuration

The deployment uses `local-path` storage class by default. Make sure you have the local-path provisioner installed:

```bash
kubectl apply -f https://raw.githubusercontent.com/rancher/local-path-provisioner/master/deploy/local-path-storage.yaml
```

## 📋 Included Resources

- **namespace.yaml**: n8n namespace
- **postgres-secret.yaml**: PostgreSQL credentials
- **postgres-configmap.yaml**: Database initialization script
- **postgres-claim0-persistentvolumeclaim.yaml**: PostgreSQL persistent storage
- **postgres-deployment.yaml**: PostgreSQL database deployment
- **postgres-service.yaml**: PostgreSQL service
- **n8n-claim0-persistentvolumeclaim.yaml**: n8n persistent storage
- **n8n-deployment.yaml**: n8n application deployment
- **n8n-service.yaml**: n8n LoadBalancer service
- **deploy.sh**: Automated deployment script
- **cleanup.sh**: Cleanup script

## 🌐 Accessing n8n

### Port Forward (Local Access)
```bash
kubectl port-forward svc/n8n 5678:5678 -n n8n
```
Then access n8n at: http://localhost:5678

### LoadBalancer (External Access)
```bash
kubectl get svc n8n -n n8n
```
Use the external IP provided by your cloud provider.

## 🔍 Troubleshooting

### Check Pod Status
```bash
kubectl get pods -n n8n
kubectl describe pod <pod-name> -n n8n
```

### Check PVC Status
```bash
kubectl get pvc -n n8n
kubectl describe pvc <pvc-name> -n n8n
```

### Check Logs
```bash
# n8n logs
kubectl logs -f deployment/n8n -n n8n

# PostgreSQL logs
kubectl logs -f deployment/postgres -n n8n
```

### Common Issues

1. **PVC Stuck in Pending**: This is normal for local-path provisioner until a pod uses it
2. **Namespace Stuck in Terminating**: Run `./cleanup.sh` to force cleanup
3. **Pod CrashLoopBackOff**: Check logs and verify database connection

## 🧹 Cleanup

To remove all resources:

```bash
./cleanup.sh
```

Or manually:

```bash
kubectl delete namespace n8n --force --grace-period=0
```

## 🏭 Production Considerations

- Replace `local-path` storage class with your cloud provider's storage class
- Configure proper resource limits and requests
- Set up ingress controllers for external access
- Enable SSL/TLS certificates
- Configure backup strategies for PostgreSQL data
- Set up monitoring and alerting

## 🌍 Supported Platforms

This deployment works on:
- [AWS EKS](https://docs.n8n.io/hosting/server-setups/aws/)
- [Azure AKS](https://docs.n8n.io/hosting/server-setups/azure/)
- [Google GKE](https://docs.n8n.io/hosting/server-setups/google-cloud/)
- Local clusters (k3s, minikube, kind)

## 📚 Additional Resources

- [n8n Official Documentation](https://docs.n8n.io/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Local-path Provisioner](https://github.com/rancher/local-path-provisioner)
