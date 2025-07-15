# Scripts Module

The scripts module contains build, deployment, and utility scripts for the Lead Intelligence Panel project.

## 🏗️ Purpose

This module provides:
- **Build Scripts**: Automated build processes for frontend and backend
- **Deployment Scripts**: Production deployment automation
- **Database Scripts**: Database management and migration scripts
- **Utility Scripts**: Development and maintenance utilities
- **CI/CD Scripts**: Continuous integration and deployment automation

## 📁 Directory Structure

```
scripts/
├── build/                  # Build automation scripts
│   ├── build-frontend.sh   # Frontend build script
│   ├── build-backend.sh    # Backend build script
│   ├── build-all.sh        # Complete project build
│   └── optimize-assets.sh  # Asset optimization
├── deploy/                 # Deployment scripts
│   ├── deploy-production.sh # Production deployment
│   ├── deploy-staging.sh   # Staging deployment
│   ├── rollback.sh         # Deployment rollback
│   └── health-check.sh     # Health check verification
├── database/               # Database management scripts
│   ├── migrate.sh          # Database migration
│   ├── seed.sh             # Database seeding
│   ├── backup.sh           # Database backup
│   └── reset.sh            # Database reset
├── dev/                    # Development utilities
│   ├── setup-dev.sh        # Development environment setup
│   ├── clean.sh            # Clean build artifacts
│   ├── lint-all.sh         # Lint all code
│   └── test-all.sh         # Run all tests
├── docker/                 # Docker-related scripts
│   ├── build-images.sh     # Build Docker images
│   ├── run-containers.sh   # Run Docker containers
│   ├── stop-containers.sh  # Stop Docker containers
│   └── clean-images.sh     # Clean Docker images
├── ci/                     # CI/CD scripts
│   ├── ci-build.sh         # CI build process
│   ├── ci-test.sh          # CI testing process
│   ├── ci-deploy.sh        # CI deployment process
│   └── ci-cleanup.sh       # CI cleanup process
├── utils/                  # Utility scripts
│   ├── version-bump.sh     # Version bumping
│   ├── changelog.sh        # Changelog generation
│   ├── dependency-check.sh # Dependency checking
│   └── security-scan.sh    # Security scanning
└── README.md               # This file
```

## 🚀 Quick Start

### Prerequisites

- **Bash**: Unix-like shell environment
- **Node.js**: Node.js runtime
- **pnpm**: Package manager
- **Docker**: Containerization (optional)
- **Git**: Version control

### Making Scripts Executable

```bash
# Make all scripts executable
chmod +x scripts/**/*.sh

# Or make specific scripts executable
chmod +x scripts/build/build-all.sh
chmod +x scripts/deploy/deploy-production.sh
```

## 📋 Build Scripts

### Complete Build

```bash
# Build entire project
./scripts/build/build-all.sh

# Build with specific options
./scripts/build/build-all.sh --production --optimize
```

### Frontend Build

```bash
# Build frontend only
./scripts/build/build-frontend.sh

# Build with specific environment
./scripts/build/build-frontend.sh --env production
```

### Backend Build

```bash
# Build backend only
./scripts/build/build-backend.sh

# Build with TypeScript compilation
./scripts/build/build-backend.sh --typescript
```

### Asset Optimization

```bash
# Optimize all assets
./scripts/build/optimize-assets.sh

# Optimize specific asset types
./scripts/build/optimize-assets.sh --images --css
```

## 🚀 Deployment Scripts

### Production Deployment

```bash
# Deploy to production
./scripts/deploy/deploy-production.sh

# Deploy with specific version
./scripts/deploy/deploy-production.sh --version 1.2.3

# Deploy with rollback capability
./scripts/deploy/deploy-production.sh --rollback-enabled
```

### Staging Deployment

```bash
# Deploy to staging
./scripts/deploy/deploy-staging.sh

# Deploy with database migration
./scripts/deploy/deploy-staging.sh --migrate
```

### Health Checks

```bash
# Run health checks
./scripts/deploy/health-check.sh

# Check specific services
./scripts/deploy/health-check.sh --api --frontend --database
```

### Rollback

```bash
# Rollback to previous version
./scripts/deploy/rollback.sh

# Rollback to specific version
./scripts/deploy/rollback.sh --version 1.2.2
```

## 🗄️ Database Scripts

### Migration

```bash
# Run database migrations
./scripts/database/migrate.sh

# Run specific migration
./scripts/database/migrate.sh --migration 20231201_add_users_table
```

### Seeding

```bash
# Seed database with sample data
./scripts/database/seed.sh

# Seed specific data
./scripts/database/seed.sh --users --leads --companies
```

### Backup

```bash
# Create database backup
./scripts/database/backup.sh

# Backup with timestamp
./scripts/database/backup.sh --timestamp

# Backup to specific location
./scripts/database/backup.sh --output /backups/
```

### Reset

```bash
# Reset database (DANGER: destroys all data)
./scripts/database/reset.sh

# Reset with confirmation
./scripts/database/reset.sh --confirm
```

## 🛠️ Development Scripts

### Environment Setup

```bash
# Set up development environment
./scripts/dev/setup-dev.sh

# Set up with specific options
./scripts/dev/setup-dev.sh --database --redis --docker
```

### Code Quality

```bash
# Run all linting
./scripts/dev/lint-all.sh

# Lint specific directories
./scripts/dev/lint-all.sh --frontend --backend

# Run all tests
./scripts/dev/test-all.sh

# Test with coverage
./scripts/dev/test-all.sh --coverage
```

### Cleanup

```bash
# Clean build artifacts
./scripts/dev/clean.sh

# Clean specific artifacts
./scripts/dev/clean.sh --node-modules --dist --coverage
```

## 🐳 Docker Scripts

### Image Management

```bash
# Build all Docker images
./scripts/docker/build-images.sh

# Build specific images
./scripts/docker/build-images.sh --frontend --backend

# Clean Docker images
./scripts/docker/clean-images.sh
```

### Container Management

```bash
# Run all containers
./scripts/docker/run-containers.sh

# Run with specific configuration
./scripts/docker/run-containers.sh --env production

# Stop all containers
./scripts/docker/stop-containers.sh

# Stop specific containers
./scripts/docker/stop-containers.sh --frontend --backend
```

## 🔄 CI/CD Scripts

### Build Process

```bash
# CI build process
./scripts/ci/ci-build.sh

# Build with caching
./scripts/ci/ci-build.sh --cache
```

### Testing Process

```bash
# CI testing process
./scripts/ci/ci-test.sh

# Test with parallel execution
./scripts/ci/ci-test.sh --parallel
```

### Deployment Process

```bash
# CI deployment process
./scripts/ci/ci-deploy.sh

# Deploy to specific environment
./scripts/ci/ci-deploy.sh --environment staging
```

### Cleanup Process

```bash
# CI cleanup process
./scripts/ci/ci-cleanup.sh

# Cleanup with specific options
./scripts/ci/ci-cleanup.sh --artifacts --cache
```

## 🛠️ Utility Scripts

### Version Management

```bash
# Bump version
./scripts/utils/version-bump.sh

# Bump specific version type
./scripts/utils/version-bump.sh --patch
./scripts/utils/version-bump.sh --minor
./scripts/utils/version-bump.sh --major
```

### Changelog Generation

```bash
# Generate changelog
./scripts/utils/changelog.sh

# Generate since specific version
./scripts/utils/changelog.sh --since 1.0.0
```

### Dependency Management

```bash
# Check dependencies
./scripts/utils/dependency-check.sh

# Check for security vulnerabilities
./scripts/utils/dependency-check.sh --security
```

### Security Scanning

```bash
# Run security scan
./scripts/utils/security-scan.sh

# Scan specific directories
./scripts/utils/security-scan.sh --frontend --backend
```

## ⚙️ Configuration

### Environment Variables

Scripts use environment variables for configuration:

```bash
# Required environment variables
export NODE_ENV=production
export DATABASE_URL=postgresql://user:pass@localhost:5432/db
export API_URL=https://api.example.com
export FRONTEND_URL=https://app.example.com

# Optional environment variables
export DOCKER_REGISTRY=your-registry.com
export DEPLOYMENT_KEY=your-deployment-key
export BACKUP_PATH=/backups/
```

### Script Configuration

Some scripts support configuration files:

```bash
# Configuration file example
# scripts/config/deployment.conf
DEPLOYMENT_ENVIRONMENT=production
ROLLBACK_ENABLED=true
HEALTH_CHECK_TIMEOUT=30
BACKUP_RETENTION_DAYS=7
```

## 🔒 Security Considerations

### Script Security

- **Input Validation**: All scripts validate inputs
- **Error Handling**: Comprehensive error handling
- **Logging**: Detailed logging for debugging
- **Permissions**: Proper file permissions

### Best Practices

- **Never run scripts as root** unless absolutely necessary
- **Review scripts** before execution
- **Use environment variables** for sensitive data
- **Test scripts** in staging before production

## 🧪 Testing Scripts

### Running Script Tests

```bash
# Test all scripts
./scripts/test/test-scripts.sh

# Test specific script category
./scripts/test/test-scripts.sh --build
./scripts/test/test-scripts.sh --deploy
```

### Script Validation

```bash
# Validate script syntax
./scripts/test/validate-scripts.sh

# Check for common issues
./scripts/test/validate-scripts.sh --lint
```

## 📚 Documentation

### Script Documentation

Each script includes:
- **Usage**: How to use the script
- **Options**: Available command-line options
- **Examples**: Practical usage examples
- **Dependencies**: Required dependencies
- **Error Codes**: Possible error codes and meanings

### Adding New Scripts

When adding new scripts:

1. **Follow naming conventions**: Use descriptive names
2. **Add documentation**: Include comprehensive help
3. **Handle errors**: Implement proper error handling
4. **Add tests**: Create tests for the script
5. **Update this README**: Document the new script

## 🤝 Contributing

### Script Development Guidelines

1. **Use Bash**: Write scripts in Bash for portability
2. **Error Handling**: Implement comprehensive error handling
3. **Logging**: Add detailed logging for debugging
4. **Documentation**: Include help and usage information
5. **Testing**: Write tests for all scripts

### Submitting Scripts

1. **Fork the repository**
2. **Create a feature branch**
3. **Add your script**
4. **Write tests**
5. **Update documentation**
6. **Submit a pull request**

## 📄 License

This module is part of the Lead Intelligence Panel project and follows the same license terms. 