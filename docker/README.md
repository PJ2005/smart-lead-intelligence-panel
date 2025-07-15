# Docker Module

The Docker module provides containerization configuration for the Lead Intelligence Panel, enabling consistent deployment across different environments.

## 🏗️ Purpose

This module provides:
- **Containerization**: Docker images for frontend, backend, and database
- **Orchestration**: Docker Compose for local development and testing
- **Production Deployment**: Production-ready Docker configurations
- **CI/CD Integration**: Docker images for continuous deployment
- **Environment Management**: Multi-environment Docker configurations

## 📁 Directory Structure

```
docker/
├── frontend/               # Frontend Docker configuration
│   ├── Dockerfile         # Frontend Docker image
│   ├── Dockerfile.dev     # Development Docker image
│   ├── nginx.conf         # Nginx configuration
│   └── .dockerignore      # Frontend ignore file
├── backend/               # Backend Docker configuration
│   ├── Dockerfile         # Backend Docker image
│   ├── Dockerfile.dev     # Development Docker image
│   ├── docker-entrypoint.sh # Entrypoint script
│   └── .dockerignore      # Backend ignore file
├── database/              # Database Docker configuration
│   ├── Dockerfile         # Database Docker image
│   ├── init.sql           # Database initialization
│   └── postgresql.conf    # PostgreSQL configuration
├── nginx/                 # Nginx reverse proxy
│   ├── Dockerfile         # Nginx Docker image
│   ├── nginx.conf         # Main nginx configuration
│   ├── ssl/               # SSL certificates
│   └── conf.d/            # Site configurations
├── redis/                 # Redis cache configuration
│   ├── Dockerfile         # Redis Docker image
│   └── redis.conf         # Redis configuration
├── compose/               # Docker Compose configurations
│   ├── docker-compose.yml # Main development compose
│   ├── docker-compose.prod.yml # Production compose
│   ├── docker-compose.test.yml # Testing compose
│   └── docker-compose.override.yml # Local overrides
├── scripts/               # Docker utility scripts
│   ├── build-images.sh    # Build all images
│   ├── run-dev.sh         # Run development environment
│   ├── run-prod.sh        # Run production environment
│   └── cleanup.sh         # Clean up containers and images
└── README.md              # This file
```

## 🚀 Quick Start

### Prerequisites

- **Docker**: Docker Engine 20.10+
- **Docker Compose**: Docker Compose 2.0+
- **Make**: GNU Make (optional, for convenience)

### Development Environment

```bash
# Start development environment
docker-compose -f docker/compose/docker-compose.yml up -d

# Start with specific services
docker-compose -f docker/compose/docker-compose.yml up -d frontend backend

# View logs
docker-compose -f docker/compose/docker-compose.yml logs -f
```

### Production Environment

```bash
# Start production environment
docker-compose -f docker/compose/docker-compose.prod.yml up -d

# Start with specific configuration
docker-compose -f docker/compose/docker-compose.prod.yml --env-file .env.prod up -d
```

## 🐳 Docker Images

### Frontend Image

```dockerfile
# docker/frontend/Dockerfile
FROM node:18-alpine AS builder

WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

### Backend Image

```dockerfile
# docker/backend/Dockerfile
FROM node:18-alpine

WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm ci --only=production

# Copy application code
COPY . .

# Create non-root user
RUN addgroup -g 1001 -S nodejs
RUN adduser -S nodejs -u 1001

# Change ownership
RUN chown -R nodejs:nodejs /app
USER nodejs

EXPOSE 8000
CMD ["npm", "start"]
```

### Database Image

```dockerfile
# docker/database/Dockerfile
FROM postgres:15-alpine

# Copy initialization scripts
COPY init.sql /docker-entrypoint-initdb.d/
COPY postgresql.conf /etc/postgresql/postgresql.conf

# Set environment variables
ENV POSTGRES_DB=lead_intelligence
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=password

EXPOSE 5432
```

## 🔧 Docker Compose Configurations

### Development Configuration

```yaml
# docker/compose/docker-compose.yml
version: '3.8'

services:
  frontend:
    build:
      context: ../../frontend
      dockerfile: ../docker/frontend/Dockerfile.dev
    ports:
      - "3000:3000"
    volumes:
      - ../../frontend:/app
      - /app/node_modules
    environment:
      - NODE_ENV=development
    depends_on:
      - backend

  backend:
    build:
      context: ../../backend
      dockerfile: ../docker/backend/Dockerfile.dev
    ports:
      - "8000:8000"
    volumes:
      - ../../backend:/app
      - /app/node_modules
    environment:
      - NODE_ENV=development
      - DATABASE_URL=postgresql://postgres:password@database:5432/lead_intelligence
    depends_on:
      - database
      - redis

  database:
    build:
      context: ../database
      dockerfile: Dockerfile
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=lead_intelligence
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=password

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data

  nginx:
    build:
      context: ../nginx
      dockerfile: Dockerfile
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ../../frontend/dist:/usr/share/nginx/html
      - ../nginx/conf.d:/etc/nginx/conf.d
    depends_on:
      - frontend
      - backend

volumes:
  postgres_data:
  redis_data:
```

### Production Configuration

```yaml
# docker/compose/docker-compose.prod.yml
version: '3.8'

services:
  frontend:
    build:
      context: ../../frontend
      dockerfile: ../docker/frontend/Dockerfile
    environment:
      - NODE_ENV=production
    restart: unless-stopped

  backend:
    build:
      context: ../../backend
      dockerfile: ../docker/backend/Dockerfile
    environment:
      - NODE_ENV=production
      - DATABASE_URL=${DATABASE_URL}
      - REDIS_URL=${REDIS_URL}
    restart: unless-stopped
    depends_on:
      - database
      - redis

  database:
    image: postgres:15-alpine
    environment:
      - POSTGRES_DB=${POSTGRES_DB}
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: unless-stopped

  redis:
    image: redis:7-alpine
    volumes:
      - redis_data:/data
    restart: unless-stopped

  nginx:
    build:
      context: ../nginx
      dockerfile: Dockerfile
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ../nginx/ssl:/etc/nginx/ssl
    restart: unless-stopped

volumes:
  postgres_data:
  redis_data:
```

## 🛠️ Docker Scripts

### Build Scripts

```bash
# Build all images
./docker/scripts/build-images.sh

# Build specific images
./docker/scripts/build-images.sh --frontend --backend

# Build with no cache
./docker/scripts/build-images.sh --no-cache
```

### Development Scripts

```bash
# Start development environment
./docker/scripts/run-dev.sh

# Start with specific services
./docker/scripts/run-dev.sh --frontend --backend

# Stop development environment
./docker/scripts/run-dev.sh --stop
```

### Production Scripts

```bash
# Start production environment
./docker/scripts/run-prod.sh

# Start with specific configuration
./docker/scripts/run-prod.sh --env-file .env.prod

# Stop production environment
./docker/scripts/run-prod.sh --stop
```

### Cleanup Scripts

```bash
# Clean up containers and images
./docker/scripts/cleanup.sh

# Clean up specific resources
./docker/scripts/cleanup.sh --containers --images --volumes
```

## 🔧 Configuration

### Environment Variables

```bash
# Database Configuration
POSTGRES_DB=lead_intelligence
POSTGRES_USER=postgres
POSTGRES_PASSWORD=secure_password

# Application Configuration
NODE_ENV=production
DATABASE_URL=postgresql://postgres:secure_password@database:5432/lead_intelligence
REDIS_URL=redis://redis:6379

# External Services
API_URL=https://api.example.com
FRONTEND_URL=https://app.example.com
```

### Nginx Configuration

```nginx
# docker/nginx/nginx.conf
events {
    worker_connections 1024;
}

http {
    upstream frontend {
        server frontend:3000;
    }

    upstream backend {
        server backend:8000;
    }

    server {
        listen 80;
        server_name localhost;

        location / {
            proxy_pass http://frontend;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
        }

        location /api {
            proxy_pass http://backend;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
        }
    }
}
```

### PostgreSQL Configuration

```conf
# docker/database/postgresql.conf
max_connections = 100
shared_buffers = 128MB
effective_cache_size = 512MB
maintenance_work_mem = 64MB
checkpoint_completion_target = 0.9
wal_buffers = 16MB
default_statistics_target = 100
random_page_cost = 1.1
effective_io_concurrency = 200
work_mem = 4MB
min_wal_size = 1GB
max_wal_size = 4GB
```

## 🔒 Security

### Security Best Practices

- **Non-root Users**: All containers run as non-root users
- **Secrets Management**: Use Docker secrets for sensitive data
- **Network Isolation**: Use custom networks for service communication
- **Image Scanning**: Regular security scanning of Docker images
- **Minimal Images**: Use minimal base images (Alpine Linux)

### Security Configuration

```yaml
# Security-focused service configuration
services:
  backend:
    security_opt:
      - no-new-privileges:true
    read_only: true
    tmpfs:
      - /tmp
      - /var/tmp
    cap_drop:
      - ALL
    cap_add:
      - CHOWN
      - SETGID
      - SETUID
```

## 📊 Monitoring

### Health Checks

```yaml
# Health check configuration
services:
  backend:
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s

  database:
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 30s
      timeout: 10s
      retries: 3
```

### Logging

```yaml
# Logging configuration
services:
  backend:
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"

  database:
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
```

## 🚀 Deployment

### Local Development

```bash
# Start all services
docker-compose -f docker/compose/docker-compose.yml up -d

# View service status
docker-compose -f docker/compose/docker-compose.yml ps

# View logs
docker-compose -f docker/compose/docker-compose.yml logs -f backend
```

### Production Deployment

```bash
# Build and deploy
docker-compose -f docker/compose/docker-compose.prod.yml up -d --build

# Scale services
docker-compose -f docker/compose/docker-compose.prod.yml up -d --scale backend=3

# Update services
docker-compose -f docker/compose/docker-compose.prod.yml pull
docker-compose -f docker/compose/docker-compose.prod.yml up -d
```

### CI/CD Integration

```yaml
# GitHub Actions example
name: Deploy to Production

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Build and push Docker images
        run: |
          docker build -t ${{ secrets.REGISTRY }}/frontend:${{ github.sha }} ./frontend
          docker build -t ${{ secrets.REGISTRY }}/backend:${{ github.sha }} ./backend
          docker push ${{ secrets.REGISTRY }}/frontend:${{ github.sha }}
          docker push ${{ secrets.REGISTRY }}/backend:${{ github.sha }}
      
      - name: Deploy to production
        run: |
          docker-compose -f docker/compose/docker-compose.prod.yml up -d
```

## 🧪 Testing

### Docker Testing

```bash
# Run tests in containers
docker-compose -f docker/compose/docker-compose.test.yml up --abort-on-container-exit

# Run specific test suite
docker-compose -f docker/compose/docker-compose.test.yml run --rm backend npm test

# Run integration tests
docker-compose -f docker/compose/docker-compose.test.yml run --rm backend npm run test:integration
```

### Test Configuration

```yaml
# docker/compose/docker-compose.test.yml
version: '3.8'

services:
  test-database:
    image: postgres:15-alpine
    environment:
      - POSTGRES_DB=test_db
      - POSTGRES_USER=test_user
      - POSTGRES_PASSWORD=test_password
    ports:
      - "5433:5432"

  backend-test:
    build:
      context: ../../backend
      dockerfile: ../docker/backend/Dockerfile.dev
    environment:
      - NODE_ENV=test
      - DATABASE_URL=postgresql://test_user:test_password@test-database:5432/test_db
    depends_on:
      - test-database
    command: npm test
```

## 📚 Documentation

### Docker Commands Reference

```bash
# Build images
docker build -t lead-intelligence-frontend ./frontend
docker build -t lead-intelligence-backend ./backend

# Run containers
docker run -d -p 3000:3000 lead-intelligence-frontend
docker run -d -p 8000:8000 lead-intelligence-backend

# View logs
docker logs -f container_name

# Execute commands in containers
docker exec -it container_name /bin/sh

# Stop and remove containers
docker stop container_name
docker rm container_name
```

### Troubleshooting

Common issues and solutions:

1. **Port conflicts**: Change port mappings in docker-compose.yml
2. **Permission issues**: Check file permissions and user configurations
3. **Memory issues**: Adjust memory limits for containers
4. **Network issues**: Check Docker network configuration

## 🤝 Contributing

### Docker Development Guidelines

1. **Use multi-stage builds** for production images
2. **Minimize image layers** to reduce size
3. **Use .dockerignore** to exclude unnecessary files
4. **Follow security best practices**
5. **Document all configurations**

### Adding New Services

1. **Create Dockerfile** for the new service
2. **Add to docker-compose.yml**
3. **Configure networking** and dependencies
4. **Add health checks** and logging
5. **Update documentation**

## 📄 License

This module is part of the Lead Intelligence Panel project and follows the same license terms. 