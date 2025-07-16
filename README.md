# Agentic AI N8n Workflow Setup Example

This repository provides various deployment configurations for hosting n8n (a workflow automation tool) using different deployment methods including Docker Compose, Kubernetes, and Caddy reverse proxy setups.

## 🚀 Quick Start

n8n is a powerful workflow automation tool that allows you to connect different services and automate processes. This repository contains multiple deployment configurations to help you get started with self-hosting n8n.

## 📁 Repository Structure

```
├── docker-compose/          # Docker Compose configurations
│   ├── withPostgres/        # n8n with PostgreSQL database
│   ├── withPostgresAndWorker/ # n8n with PostgreSQL and separate worker
│   └── subfolderWithSSL/    # n8n on subfolder with SSL
├── docker-caddy/           # Caddy reverse proxy setup
├── kubernetes/             # Kubernetes deployment manifests
└── README.md              # This file
```

## 🐳 Docker Compose Deployments

### Basic Setup with PostgreSQL
The most common setup for production use with a PostgreSQL database backend.

**Location**: `docker-compose/withPostgres/`

**Features**:
- PostgreSQL database for data persistence
- Environment-based configuration
- Production-ready setup

**Quick Start**:
```bash
cd docker-compose/withPostgres/
# Edit .env file with your credentials
docker-compose up -d
```

### Scaled Setup with Worker
For high-volume workflows, includes a separate worker container for better performance.

**Location**: `docker-compose/withPostgresAndWorker/`

**Features**:
- PostgreSQL database
- Separate worker container for processing
- Better performance for heavy workloads

**Quick Start**:
```bash
cd docker-compose/withPostgresAndWorker/
# Edit .env file with your credentials
docker-compose up -d
```

### Subfolder with SSL
Deploy n8n on a subfolder with SSL support, useful for existing web infrastructure.

**Location**: `docker-compose/subfolderWithSSL/`

**Features**:
- SSL/TLS support
- Subfolder deployment
- Reverse proxy configuration

**Quick Start**:
```bash
cd docker-compose/subfolderWithSSL/
# Edit .env file with your credentials
docker-compose up -d
```

## 🌐 Caddy Reverse Proxy Setup

**Location**: `docker-caddy/`

A complete setup using Caddy as a reverse proxy with automatic HTTPS certificates.

**Features**:
- Automatic SSL certificates via Let's Encrypt
- Easy domain configuration
- Production-ready reverse proxy

**Supported Platforms**:
- DigitalOcean
- Hetzner Cloud

## ☸️ Kubernetes Deployment

**Location**: `kubernetes/`

Complete Kubernetes manifests for deploying n8n in a Kubernetes cluster.

**Features**:
- Scalable deployment
- Persistent volume claims
- ConfigMaps and Secrets
- Service definitions

**Supported Cloud Providers**:
- AWS (Amazon Web Services)
- Azure (Microsoft Azure)
- Google Cloud Platform (GCP)

**Resources Included**:
- n8n deployment and service
- PostgreSQL deployment and service
- Persistent volume claims
- ConfigMaps and secrets

## ⚙️ Configuration

### Environment Variables
All Docker Compose setups use `.env` files for configuration. Key variables include:

```env
# Database Configuration
POSTGRES_DB=n8n
POSTGRES_USER=n8n
POSTGRES_PASSWORD=your_secure_password

# n8n Configuration
N8N_BASIC_AUTH_ACTIVE=true
N8N_BASIC_AUTH_USER=admin
N8N_BASIC_AUTH_PASSWORD=your_secure_password
```

### Security Considerations
⚠️ **Important**: Always change default passwords before deployment!

- Update database credentials in `.env` files
- Set strong passwords for n8n authentication
- Configure SSL/TLS for production deployments
- Review network security settings

## 📚 Documentation Links

- [n8n Official Documentation](https://docs.n8n.io/)
- [DigitalOcean Tutorial](https://docs.n8n.io/hosting/server-setups/digital-ocean/)
- [Hetzner Cloud Tutorial](https://docs.n8n.io/hosting/server-setups/hetzner/)
- [AWS Deployment Guide](https://docs.n8n.io/hosting/server-setups/aws/)
- [Azure Deployment Guide](https://docs.n8n.io/hosting/server-setups/azure/)
- [Google Cloud Platform Guide](https://docs.n8n.io/hosting/server-setups/google-cloud/)

## 🔧 Prerequisites

Self-hosting n8n requires technical knowledge, including:

- Setting up and configuring servers and containers
- Managing application resources and scaling
- Securing servers and applications
- Configuring n8n workflows

**Note**: n8n recommends self-hosting for expert users. Mistakes can lead to data loss, security issues, and downtime. If you aren't experienced at managing servers, consider [n8n Cloud](https://n8n.io/cloud/).

## 🔧 Troubleshooting

### Kubernetes Issues

#### PersistentVolumeClaim Stuck in Pending State
If your PVC shows as "Pending" status, this is often normal behavior for local-path storage provisioner:

```bash
# Check PVC status
kubectl get pvc -n n8n

# Describe PVC for detailed information
kubectl describe pvc n8n-claim0 -n n8n
```

**Common causes and solutions**:

1. **Local-path provisioner behavior**: The local-path storage provisioner waits for a pod to use the PVC before creating the volume. This is expected behavior.

2. **Missing storage provisioner**: Ensure the local-path provisioner is running:
   ```bash
   kubectl get pods -n kube-system | grep local-path
   ```

3. **Node selection**: The provisioner will select a node automatically when a pod is scheduled.

#### Pod Stuck in Pending State
```bash
# Check pod status
kubectl get pods -n n8n

# Describe pod for events
kubectl describe pod <pod-name> -n n8n
```

**Common solutions**:
- Ensure sufficient resources (CPU/Memory) on nodes
- Check if PVC is bound
- Verify node selectors and tolerations

#### Checking Logs
```bash
# n8n application logs
kubectl logs -n n8n deployment/n8n

# PostgreSQL logs
kubectl logs -n n8n deployment/postgres
```

### Docker Compose Issues

#### Permission Denied Errors
```bash
# Fix file permissions
sudo chown -R 1000:1000 ~/.n8n
```

#### Database Connection Issues
- Verify database credentials in `.env` file
- Check if PostgreSQL container is running
- Ensure network connectivity between containers

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

For common changes, please open a PR to the `main` branch. If you have a contribution specific to a cloud provider or deployment method, please indicate this in your PR description.

## 📄 License

This project contains configurations and examples for deploying n8n. Please refer to individual folders for specific license information.

## 🆘 Support

If you have questions after trying the tutorials, check out:
- [n8n Community Forums](https://community.n8n.io/)
- [n8n Documentation](https://docs.n8n.io/)
- [GitHub Issues](https://github.com/n8n-io/n8n/issues)

## 🏃‍♂️ Getting Started

1. Choose your deployment method (Docker Compose, Kubernetes, or Caddy)
2. Navigate to the appropriate folder
3. Follow the README instructions in that folder
4. Configure your environment variables
5. Deploy and start automating!
