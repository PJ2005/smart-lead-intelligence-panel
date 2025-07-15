# Architecture Guide

## 🏗️ System Architecture

The Lead Intelligence Panel follows a modular, microservices-inspired architecture designed for scalability, maintainability, and performance.

## 📋 Architecture Overview

### High-Level Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │    Backend      │    │   Database      │
│   (React)       │◄──►│   (Node.js)     │◄──►│  (PostgreSQL)   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Nginx         │    │     Redis       │    │   File Storage  │
│  (Reverse Proxy)│    │    (Cache)      │    │   (Uploads)     │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Technology Stack

#### Frontend
- **Framework**: React 18 with TypeScript
- **Build Tool**: Vite
- **State Management**: Zustand
- **UI Library**: Material-UI or Chakra UI
- **Routing**: React Router v6
- **Testing**: Vitest + React Testing Library

#### Backend
- **Runtime**: Node.js 18+ with TypeScript
- **Framework**: Express.js or Fastify
- **Database ORM**: Prisma
- **Authentication**: JWT with bcrypt
- **Validation**: Zod
- **Testing**: Jest + Supertest

#### Database
- **Primary**: PostgreSQL 14+
- **Cache**: Redis 7+
- **Migrations**: Prisma Migrate

#### Infrastructure
- **Containerization**: Docker + Docker Compose
- **Reverse Proxy**: Nginx
- **CI/CD**: GitHub Actions
- **Monitoring**: Sentry

## 🏛️ Design Patterns

### 1. Layered Architecture

The backend follows a layered architecture pattern:

```
┌─────────────────────────────────────────────────────────┐
│                    Presentation Layer                    │
│                 (Controllers/Routes)                     │
└─────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────┐
│                     Business Layer                       │
│                    (Services/Logic)                      │
└─────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────┐
│                      Data Layer                          │
│                 (Repositories/Models)                    │
└─────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────┐
│                   Infrastructure Layer                   │
│                (Database/External APIs)                  │
└─────────────────────────────────────────────────────────┘
```

### 2. Repository Pattern

Data access is abstracted through repository interfaces:

```typescript
interface ILeadRepository {
  findById(id: string): Promise<Lead | null>;
  findAll(filters: LeadFilters): Promise<Lead[]>;
  create(lead: CreateLeadDto): Promise<Lead>;
  update(id: string, updates: UpdateLeadDto): Promise<Lead>;
  delete(id: string): Promise<void>;
}

class PrismaLeadRepository implements ILeadRepository {
  constructor(private prisma: PrismaClient) {}
  
  async findById(id: string): Promise<Lead | null> {
    return this.prisma.lead.findUnique({ where: { id } });
  }
  
  // ... other methods
}
```

### 3. Service Layer Pattern

Business logic is encapsulated in service classes:

```typescript
class LeadService {
  constructor(
    private leadRepository: ILeadRepository,
    private emailService: IEmailService,
    private analyticsService: IAnalyticsService
  ) {}
  
  async createLead(leadData: CreateLeadDto): Promise<Lead> {
    // Business logic validation
    await this.validateLeadData(leadData);
    
    // Create lead
    const lead = await this.leadRepository.create(leadData);
    
    // Send notifications
    await this.emailService.sendLeadNotification(lead);
    
    // Track analytics
    await this.analyticsService.trackLeadCreated(lead);
    
    return lead;
  }
}
```

### 4. Dependency Injection

Services use dependency injection for better testability:

```typescript
class LeadController {
  constructor(private leadService: LeadService) {}
  
  async createLead(req: Request, res: Response) {
    try {
      const lead = await this.leadService.createLead(req.body);
      res.status(201).json(lead);
    } catch (error) {
      res.status(400).json({ error: error.message });
    }
  }
}
```

## 🗄️ Database Design

### Entity Relationship Diagram

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│    Users    │    │   Companies │    │    Leads    │
├─────────────┤    ├─────────────┤    ├─────────────┤
│ id          │    │ id          │    │ id          │
│ email       │    │ name        │    │ firstName   │
│ firstName   │    │ industry    │    │ lastName    │
│ lastName    │    │ size        │    │ email       │
│ role        │    │ website     │    │ phone       │
│ companyId   │────│ createdAt   │    │ company     │
│ createdAt   │    │ updatedAt   │    │ status      │
│ updatedAt   │    └─────────────┘    │ source      │
└─────────────┘                       │ assignedTo  │
                                      │ createdAt   │
                                      │ updatedAt   │
                                      └─────────────┘
                                              │
                                              │
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│ Activities  │    │   Analytics │    │ Notifications│
├─────────────┤    ├─────────────┤    ├─────────────┤
│ id          │    │ id          │    │ id          │
│ leadId      │    │ leadId      │    │ userId      │
│ type        │    │ eventType   │    │ type        │
│ description │    │ data        │    │ message     │
│ timestamp   │    │ timestamp   │    │ read        │
│ userId      │    │ metadata    │    │ createdAt   │
└─────────────┘    └─────────────┘    └─────────────┘
```

### Database Schema

#### Users Table
```sql
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) UNIQUE NOT NULL,
  firstName VARCHAR(100) NOT NULL,
  lastName VARCHAR(100) NOT NULL,
  role USER_ROLE NOT NULL DEFAULT 'VIEWER',
  companyId UUID REFERENCES companies(id),
  passwordHash VARCHAR(255) NOT NULL,
  isActive BOOLEAN DEFAULT true,
  lastLoginAt TIMESTAMP,
  createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### Leads Table
```sql
CREATE TABLE leads (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  firstName VARCHAR(100) NOT NULL,
  lastName VARCHAR(100) NOT NULL,
  email VARCHAR(255) NOT NULL,
  phone VARCHAR(20),
  company VARCHAR(255) NOT NULL,
  status LEAD_STATUS DEFAULT 'NEW',
  source VARCHAR(100) NOT NULL,
  assignedTo UUID REFERENCES users(id),
  score INTEGER DEFAULT 0,
  notes TEXT,
  createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 🔐 Security Architecture

### Authentication Flow

1. **Login**: User provides credentials
2. **Validation**: Backend validates credentials
3. **JWT Generation**: Backend generates JWT token
4. **Token Storage**: Frontend stores token securely
5. **API Requests**: Frontend includes token in headers
6. **Token Validation**: Backend validates token on each request

### Authorization

Role-based access control (RBAC):

```typescript
enum UserRole {
  ADMIN = 'ADMIN',
  MANAGER = 'MANAGER',
  SALES_REP = 'SALES_REP',
  ANALYST = 'ANALYST',
  VIEWER = 'VIEWER'
}

const permissions = {
  [UserRole.ADMIN]: ['*'],
  [UserRole.MANAGER]: ['leads:read', 'leads:write', 'users:read'],
  [UserRole.SALES_REP]: ['leads:read', 'leads:write'],
  [UserRole.ANALYST]: ['leads:read', 'analytics:read'],
  [UserRole.VIEWER]: ['leads:read']
};
```

### Data Protection

- **Encryption**: Passwords hashed with bcrypt
- **HTTPS**: All communications encrypted
- **Input Validation**: Comprehensive input sanitization
- **Rate Limiting**: API rate limiting to prevent abuse
- **CORS**: Configured for frontend communication

## 📡 API Design

### RESTful API Structure

```
/api/v1/
├── auth/
│   ├── POST /login
│   ├── POST /register
│   ├── POST /logout
│   └── POST /refresh
├── users/
│   ├── GET /
│   ├── GET /:id
│   ├── PUT /:id
│   └── DELETE /:id
├── leads/
│   ├── GET /
│   ├── GET /:id
│   ├── POST /
│   ├── PUT /:id
│   ├── DELETE /:id
│   └── GET /analytics
├── companies/
│   ├── GET /
│   ├── GET /:id
│   └── POST /
└── analytics/
    ├── GET /dashboard
    ├── GET /leads
    └── GET /performance
```

### API Response Format

```typescript
interface ApiResponse<T> {
  success: boolean;
  data?: T;
  error?: string;
  message?: string;
  pagination?: {
    page: number;
    limit: number;
    total: number;
    totalPages: number;
  };
}
```

### Error Handling

Standardized error responses:

```typescript
class ApiError extends Error {
  constructor(
    public statusCode: number,
    public message: string,
    public code?: string
  ) {
    super(message);
  }
}

// Error middleware
app.use((error: ApiError, req: Request, res: Response, next: NextFunction) => {
  res.status(error.statusCode || 500).json({
    success: false,
    error: error.message,
    code: error.code
  });
});
```

## 🔄 Real-time Communication

### WebSocket Architecture

```typescript
// WebSocket event types
enum WebSocketEvent {
  LEAD_CREATED = 'lead:created',
  LEAD_UPDATED = 'lead:updated',
  LEAD_DELETED = 'lead:deleted',
  NOTIFICATION = 'notification',
  USER_ACTIVITY = 'user:activity'
}

// WebSocket connection management
class WebSocketManager {
  private connections = new Map<string, WebSocket>();
  
  broadcast(event: WebSocketEvent, data: any) {
    this.connections.forEach(ws => {
      ws.send(JSON.stringify({ event, data }));
    });
  }
}
```

## 📊 Performance Considerations

### Caching Strategy

- **Redis Cache**: Session storage and API response caching
- **Browser Cache**: Static assets and API responses
- **Database Query Optimization**: Indexed queries and connection pooling

### Database Optimization

```sql
-- Indexes for performance
CREATE INDEX idx_leads_status ON leads(status);
CREATE INDEX idx_leads_assigned_to ON leads(assignedTo);
CREATE INDEX idx_leads_created_at ON leads(createdAt);
CREATE INDEX idx_activities_lead_id ON activities(leadId);
```

### Frontend Optimization

- **Code Splitting**: Route-based code splitting
- **Lazy Loading**: Component lazy loading
- **Image Optimization**: Compressed and optimized images
- **Bundle Analysis**: Regular bundle size monitoring

## 🧪 Testing Strategy

### Testing Pyramid

```
        /\
       /  \     E2E Tests (Few)
      /____\    
     /      \   Integration Tests (Some)
    /________\  
   /          \ Unit Tests (Many)
  /____________\
```

### Test Types

1. **Unit Tests**: Individual functions and components
2. **Integration Tests**: API endpoints and database operations
3. **E2E Tests**: Complete user workflows
4. **Performance Tests**: Load and stress testing

## 🚀 Deployment Architecture

### Environment Strategy

- **Development**: Local development with hot reload
- **Staging**: Production-like environment for testing
- **Production**: Optimized and monitored environment

### Container Strategy

```yaml
# Docker Compose services
services:
  frontend:
    build: ./frontend
    ports: ["3000:3000"]
    
  backend:
    build: ./backend
    ports: ["8000:8000"]
    depends_on: [database, redis]
    
  database:
    image: postgres:15
    environment:
      POSTGRES_DB: lead_intelligence
      
  redis:
    image: redis:7
    
  nginx:
    build: ./nginx
    ports: ["80:80", "443:443"]
```

## 📈 Monitoring and Observability

### Logging Strategy

- **Structured Logging**: JSON format for easy parsing
- **Log Levels**: Error, Warn, Info, Debug
- **Centralized Logging**: Aggregated logs for analysis

### Metrics Collection

- **Application Metrics**: Response times, error rates
- **Business Metrics**: Lead conversion rates, user activity
- **Infrastructure Metrics**: CPU, memory, disk usage

### Health Checks

```typescript
// Health check endpoint
app.get('/health', async (req, res) => {
  const health = {
    status: 'ok',
    timestamp: new Date().toISOString(),
    services: {
      database: await checkDatabase(),
      redis: await checkRedis(),
      external: await checkExternalServices()
    }
  };
  
  res.json(health);
});
```

## 🔄 CI/CD Pipeline

### Pipeline Stages

1. **Build**: Compile and build applications
2. **Test**: Run automated tests
3. **Security Scan**: Vulnerability scanning
4. **Deploy**: Deploy to staging/production
5. **Monitor**: Post-deployment monitoring

### GitHub Actions Workflow

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
      - run: pnpm install
      - run: pnpm test
      - run: pnpm lint
      
  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v3
      - run: docker-compose up -d --build
```

## 🔮 Future Considerations

### Scalability

- **Horizontal Scaling**: Load balancing across multiple instances
- **Database Sharding**: Partition data across multiple databases
- **Microservices**: Break down into smaller, focused services

### Technology Evolution

- **GraphQL**: Consider GraphQL for more flexible data fetching
- **Serverless**: Explore serverless functions for specific features
- **Edge Computing**: CDN-based edge functions for global performance

### Security Enhancements

- **OAuth 2.0**: Implement OAuth for third-party integrations
- **2FA**: Two-factor authentication for enhanced security
- **Audit Logging**: Comprehensive audit trail for compliance

---

This architecture provides a solid foundation for building a scalable, maintainable, and secure B2B lead intelligence platform. 