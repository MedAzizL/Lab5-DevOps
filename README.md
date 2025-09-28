# Lab 5: DevOps 3-Tier Application Deployment 🚀

**Student:** MedAzizL  
**Course:** DevOps  
**Date:** September 2025  

## 📋 Project Overview

This project demonstrates the deployment of a complete 3-tier web application using Kubernetes orchestration on Azure Cloud Platform. The application consists of a React frontend, Flask API backend, and PostgreSQL database, all containerized and deployed on Azure Kubernetes Service (AKS).

## 🏗️ Architecture

```
Internet
    ↓
Azure Load Balancer (57.152.1.133)
    ↓
Frontend Pods [2 replicas] (React + Nginx)
    ↓ /api/* proxy
Backend Pods [3 replicas] (Flask API)
    ↓ DATABASE_URL
PostgreSQL Pod [1 replica] (Database)
```

## 🛠️ Technologies Used

- **Frontend:** React.js + Nginx
- **Backend:** Python Flask API
- **Database:** PostgreSQL 15
- **Containerization:** Docker
- **Orchestration:** Kubernetes
- **Cloud Platform:** Microsoft Azure
  - Azure Kubernetes Service (AKS)
  - Azure Container Registry (ACR)
- **CI/CD Ready:** GitHub Actions workflow template

## 📁 Project Structure

```
├── app/                              # Flask backend application
│   ├── __init__.py
│   ├── config.py                    # Database configuration
│   ├── routes.py                    # API endpoints
│   ├── Dockerfile                   # Backend container config
│   ├── models/
│   └── utils/
├── static/                          # React frontend application
│   ├── src/                        # React source code
│   ├── public/                     # Static assets
│   ├── Dockerfile                  # Frontend container config
│   ├── nginx.conf                  # Nginx proxy configuration
│   └── package.json
├── kubernets/                      # Kubernetes manifests
│   ├── postgres-deployment.yaml   # Database deployment
│   ├── backend-deployment-fixed.yaml  # Backend deployment
│   └── frontend-deployment.yaml   # Frontend deployment
├── docker-compose.yml              # Local development
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

## 🚀 Deployment Instructions

### Prerequisites

- Azure CLI installed and configured
- kubectl installed
- Docker installed
- Access to Azure subscription

### Azure Resources Setup

1. **Create Resource Group:**
   ```bash
   az group create --name DevOpsLabRG --location eastus
   ```

2. **Create Azure Container Registry:**
   ```bash
   az acr create --resource-group DevOpsLabRG --name devopslabacr123 --sku Basic
   ```

3. **Create AKS Cluster:**
   ```bash
   az aks create --resource-group DevOpsLabRG --name DevOpsLabAKS --node-count 2 --enable-addons monitoring --generate-ssh-keys
   ```

4. **Connect AKS to ACR:**
   ```bash
   az aks update -g DevOpsLabRG -n DevOpsLabAKS --attach-acr devopslabacr123
   ```

### Build and Push Images

1. **Login to ACR:**
   ```bash
   az acr login --name devopslabacr123
   ```

2. **Build and push backend:**
   ```bash
   docker build -f app/Dockerfile -t devopslabacr123.azurecr.io/backend:v1 .
   docker push devopslabacr123.azurecr.io/backend:v1
   ```

3. **Build and push frontend:**
   ```bash
   docker build -t devopslabacr123.azurecr.io/frontend:v1 ./static
   docker push devopslabacr123.azurecr.io/frontend:v1
   ```

### Deploy to Kubernetes

1. **Get AKS credentials:**
   ```bash
   az aks get-credentials --resource-group DevOpsLabRG --name DevOpsLabAKS
   ```

2. **Deploy all services:**
   ```bash
   kubectl apply -f kubernets/
   ```

3. **Get external IP:**
   ```bash
   kubectl get svc frontend
   ```

## 🎯 Lab Requirements Fulfilled

| Requirement | Status | Implementation |
|-------------|--------|---------------|
| **3-tier application** | ✅ | Frontend → Backend → Database |
| **Containerization** | ✅ | Docker images for all services |
| **Kubernetes orchestration** | ✅ | Deployments, Services, ReplicaSets |
| **Scaling demonstration** | ✅ | Backend: 3 replicas, Frontend: 2 replicas |
| **Rolling updates** | ✅ | `kubectl set image` capability |
| **External access** | ✅ | LoadBalancer with public IP |
| **Service discovery** | ✅ | Internal DNS resolution |
| **Persistent storage** | ✅ | PostgreSQL with PVC |

## 🔧 Operations & Testing

### Scaling

```bash
# Scale backend
kubectl scale deployment backend --replicas=5

# Scale frontend  
kubectl scale deployment frontend --replicas=3
```

### Rolling Updates

```bash
# Build new version
docker build -f app/Dockerfile -t devopslabacr123.azurecr.io/backend:v2 .
docker push devopslabacr123.azurecr.io/backend:v2

# Deploy update
kubectl set image deployment/backend backend=devopslabacr123.azurecr.io/backend:v2
kubectl rollout status deployment/backend
```

### Monitoring

```bash
# Check pods status
kubectl get pods

# View logs
kubectl logs -l app=backend
kubectl logs -l app=frontend

# Check services
kubectl get svc
```

## 🌐 Application Access

**Live Application:** http://57.152.1.133

### Features
- User registration and authentication
- Task management (CRUD operations)
- Real-time updates
- Responsive React UI
- RESTful API backend
- Persistent data storage

### API Endpoints
- `POST /api/create_user` - User registration
- `POST /api/get_token` - User login
- `GET /api/user` - Get user data
- `POST /api/submit_task` - Create task
- `POST /api/edit_task` - Update task
- `POST /api/delete_task` - Delete task

## 🔐 Security Features

- JWT-based authentication
- Bcrypt password hashing
- Kubernetes secrets for database credentials
- Private container registry (ACR)
- Network policies (cluster internal communication)

## 📊 Performance & Scalability

- **High Availability:** Multiple replicas per service
- **Load Balancing:** Kubernetes service load balancing
- **Auto-scaling ready:** HPA can be configured
- **Rolling deployments:** Zero-downtime updates
- **Health checks:** Readiness and liveness probes

## 🚀 CI/CD Pipeline (Future Enhancement)

The project is ready for GitHub Actions CI/CD integration:

1. **Build Stage:** Build and test Docker images
2. **Push Stage:** Push images to ACR
3. **Deploy Stage:** Update Kubernetes deployments
4. **Verify Stage:** Health checks and smoke tests

## 📝 Lessons Learned

1. **Service Discovery:** Internal DNS naming in Kubernetes
2. **Configuration Management:** Environment variables vs ConfigMaps
3. **Networking:** LoadBalancer vs NodePort vs Ingress
4. **Storage:** Persistent volumes for stateful services
5. **Debugging:** Pod logs and troubleshooting techniques

## 🎓 Educational Outcomes

This lab demonstrated:
- Container orchestration with Kubernetes
- Cloud-native application deployment
- Infrastructure as Code (IaC) principles
- Microservices architecture patterns
- DevOps best practices

## 📞 Contact

**Student:** MedAzizL  
**Email:** mohamedaziz.laifi@etudiant-isi.utm.tn  
**GitHub:** https://github.com/MedAzizL/Lab5-DevOps

---

**🏆 Lab 5 Status: COMPLETED SUCCESSFULLY**