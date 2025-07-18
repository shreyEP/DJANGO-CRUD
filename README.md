# DJANGO-CRUD
 it is a simple Django Crud app

## Kubernetes Deployment

### Prerequisites

*   `kubectl`
*   A running Kubernetes cluster
*   Docker

### Build and Push the Docker Image

Build the Docker image:
```bash
docker build -t your-dockerhub-username/django-app:latest .
```

Push the Docker image to a container registry:
```bash
docker push your-dockerhub-username/django-app:latest
```

### Update Secret Files

Update the placeholder values in the following files with your actual credentials:

*   [`kubernetes/postgres-secret.yaml`](kubernetes/postgres-secret.yaml)
*   [`kubernetes/django-secret.yaml`](kubernetes/django-secret.yaml)

### Deploy to Kubernetes

Apply the Kubernetes configurations:
```bash
kubectl apply -k kubernetes/
```
This command will create all the necessary resources, including deployments, services, persistent volumes, and config maps.

### Accessing the Application

To find the external IP of the service, run the following command:
```bash
kubectl get svc django-service
```

Once you have the external IP, you can access the application in your browser at `http://<EXTERNAL-IP>`.
