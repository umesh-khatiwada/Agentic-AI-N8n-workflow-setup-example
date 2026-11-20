# Agentic AI N8n Workflow Setup Example

This repository provides various deployment configurations for hosting n8n (a workflow automation tool) using different deployment methods including Docker Compose, Kubernetes, and Caddy reverse proxy setups.

## 🚀 Quick Start

n8n is a powerful workflow automation tool that allows you to connect different services and automate processes. This repository contains multiple deployment configurations to help you get started with self-hosting n8n.

## 📁 Repository Structure

```
├── docker-compose/          # Docker Compose configurations
│   ├── withPostgres/        # n8n with PostgreSQL database
│   ├── withPostgresAndWorker/ # n8n with PostgreSQL, Redis and a queue worker
│   └── subfolderWithSSL/    # n8n on a subfolder behind Traefik with SSL
├── docker-caddy/            # n8n behind a Caddy reverse proxy
├── kubernetes/              # Kubernetes manifests (n8n + PostgreSQL, nginx ingress)
├── work-flow-example/       # Importable n8n workflow examples (agentic AI / MCP / RabbitMQ)
├── .gitleaks.toml           # Secret-scanning configuration
├── LICENSE
└── README.md                # This file
```

## 🤖 Agentic AI Workflow Examples

`work-flow-example/` contains n8n workflow JSON files you can import (n8n UI: Workflows -> Import from file). Credentials are not included; you must create your own in n8n.

| Folder | Files | What it contains (from the node graph) | Credentials needed |
|--------|-------|----------------------------------------|--------------------|
| `chatbot-that-can-communicate-with-API-endpoints/` | `chatbotmcp-client.json`, `chatbot-mcp-sever.json`, `openapi-spec.yaml`, `systemAImessage.txt` | Client: chat trigger + Gemini chat/embeddings, Google Drive triggers feeding a Qdrant vector store, an AI agent with an MCP client tool. Server: MCP server trigger exposing HTTP GET/POST/PUT and Redis tools. The OpenAPI spec and system prompt describe an example "Preferences API" the agent calls. | Google Gemini (PaLM) API, Google Drive OAuth2, Qdrant, HTTP bearer auth, Redis |
| `google-file-watcher-rabbitmq/` | `google-file-watcher-rabbitmq.json` | Google Drive trigger, file-extension check, download, convert to text, publish to RabbitMQ | Google Drive OAuth2, RabbitMQ |
| `s3-mcp-server/` | `s3-mcp-client.json`, `s3-mcp-server.json`, `s3-bucket-lamda-fucntions.py` | Chat trigger + Gemini + AI agent with an MCP client tool; a Python AWS Lambda handler that enables/suspends S3 bucket versioning via `boto3` | Google Gemini (PaLM) API; AWS credentials for the Lambda |

The API host used in `systemAImessage.txt` is an example/placeholder; TODO: document the exact MCP endpoint wiring once confirmed.

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
docker compose up -d
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
docker compose up -d
```

### Subfolder with SSL
Deploy n8n on a subfolder with SSL support, useful for existing web infrastructure.

**Location**: `docker-compose/subfolderWithSSL/`

**Features**:
- SSL/TLS support
- Subfolder deployment
- Traefik reverse proxy

**Quick Start**:
```bash
cd docker-compose/subfolderWithSSL/
# Edit .env file with your credentials
docker compose up -d
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

The manifests are generic (nginx ingress class, `local-path`-style PVCs, `postgres:11`, `n8nio/n8n`); see the cloud guides linked below for provider specifics. The ingress host in `kubernetes/n8n.ingress.yaml` is a personal domain: change it to yours. Note that `kubernetes/README.md` mentions helper scripts (`deploy.sh`, `cleanup.sh`) that are not in the repository; apply the YAML files with `kubectl` instead.

**Resources Included**:
- n8n deployment and service
- PostgreSQL deployment and service
- Persistent volume claims
- ConfigMaps and secrets

## ⚙️ Configuration

### Environment Variables
Each Docker Compose setup reads a `.env` file in its own folder (these files are committed with placeholder values; replace them with your own and avoid committing real ones):

| Setup | Variables |
|-------|-----------|
| `docker-compose/withPostgres` | `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`, `POSTGRES_NON_ROOT_USER`, `POSTGRES_NON_ROOT_PASSWORD` |
| `docker-compose/withPostgresAndWorker` | the above plus `ENCRYPTION_KEY` (passed to n8n as `N8N_ENCRYPTION_KEY`) |
| `docker-compose/subfolderWithSSL` | `DATA_FOLDER`, `DOMAIN_NAME`, `SUBFOLDER`, `N8N_PATH`, `GENERIC_TIMEZONE`, `SSL_EMAIL` |
| `docker-caddy` | `DATA_FOLDER`, `DOMAIN_NAME`, `SUBDOMAIN`, `GENERIC_TIMEZONE`, `SSL_EMAIL` |

Kubernetes credentials live in `kubernetes/postgres-secret.yaml` and `kubernetes/postgres-configmap.yaml`.

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

Released under the MIT License, see [LICENSE](LICENSE) (the existing license text carries the n8n copyright line because much of the deployment configuration derives from n8n's example setups). `docker-caddy/` ships its own `LICENSE`.

## 🆘 Support

If you have questions after trying the tutorials, check out:
- [n8n Community Forums](https://community.n8n.io/)
- [n8n Documentation](https://docs.n8n.io/)
- [n8n GitHub Issues](https://github.com/n8n-io/n8n/issues)

## 🏃‍♂️ Getting Started

1. Choose your deployment method (Docker Compose, Kubernetes, or Caddy)
2. Navigate to the appropriate folder
3. Follow the README instructions in that folder
4. Configure your environment variables
5. Deploy and start automating!

## 👤 Author

Umesh Khatiwada - [github.com/umesh-khatiwada](https://github.com/umesh-khatiwada)
