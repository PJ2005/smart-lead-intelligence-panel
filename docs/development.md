# Development Guide

This guide provides comprehensive instructions for setting up and working with the Lead Intelligence Panel development environment.

## 🚀 Quick Start

### Prerequisites

Before you begin, ensure you have the following installed:

- **Node.js**: Version 18 or higher
- **pnpm**: Version 8 or higher
- **PostgreSQL**: Version 14 or higher
- **Git**: Latest version
- **Docker**: Optional, for containerized development

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-org/lead-intelligence-panel.git
   cd lead-intelligence-panel
   ```

2. **Install dependencies**
   ```bash
   pnpm install
   ```

3. **Set up environment variables**
   ```bash
   cp env.example .env
   # Edit .env with your configuration
   ```

4. **Set up database**
   ```bash
   pnpm db:migrate
   pnpm db:seed
   ```

5. **Start development servers**
   ```bash
   pnpm dev
   ```

## 🛠️ Development Environment

### Project Structure

```
lead-intelligence-panel/
├── backend/                 # Backend application
│   ├── src/
│   │   ├── api/            # API routes and controllers
│   │   ├── services/       # Business logic services
│   │   ├── models/         # Data models and schemas
│   │   ├── middleware/     # Custom middleware
│   │   ├── utils/          # Utility functions
│   │   └── config/         # Configuration files
│   ├── tests/              # Backend tests
│   └── docs/               # Backend documentation
├── frontend/               # Frontend application
│   ├── src/
│   │   ├── components/     # Reusable UI components
│   │   ├── pages/          # Page components
│   │   ├── hooks/          # Custom React hooks
│   │   ├── services/       # API service layer
│   │   ├── store/          # State management
│   │   ├── utils/          # Utility functions
│   │   └── types/          # TypeScript types
│   ├── public/             # Static assets
│   └── docs/               # Frontend documentation
├── shared/                 # Shared code between frontend and backend
│   ├── types/              # Shared TypeScript types
│   ├── utils/              # Shared utilities
│   └── constants/          # Shared constants
├── docs/                   # Project documentation
├── scripts/                # Build and deployment scripts
└── docker/                 # Docker configuration
```

### Available Scripts

| Script | Description |
|--------|-------------|
| `pnpm dev` | Start both frontend and backend in development |
| `pnpm dev:backend` | Start backend development server |
| `pnpm dev:frontend` | Start frontend development server |
| `pnpm build` | Build both frontend and backend for production |
| `pnpm start` | Start production servers |
| `pnpm test` | Run all tests |
| `pnpm lint` | Run linting |
| `pnpm format` | Format code with Prettier |
| `pnpm type-check` | Run TypeScript type checking |
| `pnpm db:migrate` | Run database migrations |
| `pnpm db:seed` | Seed database with sample data |
| `pnpm db:reset` | Reset database |

## 🔧 Configuration

### Environment Variables

The application uses environment variables for configuration. Copy `env.example` to `.env` and configure:

```bash
# Application Configuration
NODE_ENV=development
PORT=8000
FRONTEND_PORT=3000

# Database Configuration
DATABASE_URL=postgresql://postgres:password@localhost:5432/lead_intelligence
POSTGRES_DB=lead_intelligence
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password

# Authentication
JWT_SECRET=your-super-secret-jwt-key-change-this-in-production
JWT_EXPIRES_IN=7d

# API Configuration
API_URL=http://localhost:8000
FRONTEND_URL=http://localhost:3000
CORS_ORIGIN=http://localhost:3000
```

### Database Setup

1. **Install PostgreSQL**
   ```bash
   # macOS with Homebrew
   brew install postgresql
   brew services start postgresql

   # Ubuntu/Debian
   sudo apt-get install postgresql postgresql-contrib
   sudo systemctl start postgresql
   ```

2. **Create database**
   ```bash
   createdb lead_intelligence
   ```

3. **Run migrations**
   ```bash
   pnpm db:migrate
   ```

4. **Seed with sample data**
   ```bash
   pnpm db:seed
   ```

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pnpm test

# Run backend tests only
pnpm test:backend

# Run frontend tests only
pnpm test:frontend

# Run tests with coverage
pnpm test:coverage

# Run tests in watch mode
pnpm test:watch
```

### Test Structure

- **Unit Tests**: Test individual functions and components
- **Integration Tests**: Test API endpoints and database operations
- **E2E Tests**: Test complete user workflows

### Writing Tests

```typescript
// Backend test example
describe('LeadService', () => {
  let leadService: LeadService;
  let mockRepository: jest.Mocked<ILeadRepository>;

  beforeEach(() => {
    mockRepository = createMockRepository();
    leadService = new LeadService(mockRepository);
  });

  it('should create a lead successfully', async () => {
    const leadData = { firstName: 'John', lastName: 'Doe', email: 'john@example.com' };
    const expectedLead = { id: '1', ...leadData };

    mockRepository.create.mockResolvedValue(expectedLead);

    const result = await leadService.createLead(leadData);

    expect(result).toEqual(expectedLead);
    expect(mockRepository.create).toHaveBeenCalledWith(leadData);
  });
});
```

```typescript
// Frontend test example
import { render, screen, fireEvent } from '@testing-library/react';
import { LeadForm } from './LeadForm';

describe('LeadForm', () => {
  it('should submit form with valid data', () => {
    const mockSubmit = jest.fn();
    render(<LeadForm onSubmit={mockSubmit} />);

    fireEvent.change(screen.getByLabelText(/first name/i), {
      target: { value: 'John' },
    });
    fireEvent.change(screen.getByLabelText(/last name/i), {
      target: { value: 'Doe' },
    });
    fireEvent.change(screen.getByLabelText(/email/i), {
      target: { value: 'john@example.com' },
    });

    fireEvent.click(screen.getByRole('button', { name: /create lead/i }));

    expect(mockSubmit).toHaveBeenCalledWith({
      firstName: 'John',
      lastName: 'Doe',
      email: 'john@example.com',
    });
  });
});
```

## 🔍 Code Quality

### Linting

```bash
# Run ESLint
pnpm lint

# Fix auto-fixable issues
pnpm lint:fix
```

### Code Formatting

```bash
# Format code with Prettier
pnpm format

# Check formatting without changing files
pnpm format:check
```

### Type Checking

```bash
# Run TypeScript type checking
pnpm type-check
```

### Pre-commit Hooks

The project uses Husky for pre-commit hooks that automatically:

- Run linting
- Format code
- Run type checking
- Run tests

## 🐳 Docker Development

### Using Docker

```bash
# Start development environment with Docker
pnpm docker:up

# View logs
pnpm docker:logs

# Stop containers
pnpm docker:down

# Rebuild images
pnpm docker:build
```

### Docker Compose Services

- **frontend**: React development server
- **backend**: Node.js API server
- **database**: PostgreSQL database
- **redis**: Redis cache
- **nginx**: Reverse proxy

## 📚 Development Workflow

### Feature Development

1. **Create feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make changes**
   - Write code following style guidelines
   - Add tests for new functionality
   - Update documentation if needed

3. **Test your changes**
   ```bash
   pnpm test
   pnpm lint
   pnpm type-check
   ```

4. **Commit changes**
   ```bash
   git add .
   git commit -m "feat(scope): description"
   ```

5. **Push and create PR**
   ```bash
   git push origin feature/your-feature-name
   ```

### Debugging

#### Backend Debugging

```bash
# Start backend with debugging
pnpm dev:backend:debug

# Use VS Code debugger
# Add breakpoints in your code
# Press F5 to start debugging
```

#### Frontend Debugging

```bash
# Start frontend with debugging
pnpm dev:frontend:debug

# Use browser dev tools
# Add console.log statements
# Use React DevTools extension
```

### Database Debugging

```bash
# Connect to database
psql -d lead_intelligence

# View tables
\dt

# Query data
SELECT * FROM leads LIMIT 10;

# View migrations
SELECT * FROM _prisma_migrations;
```

## 🔧 Development Tools

### VS Code Extensions

Recommended extensions for development:

- **TypeScript and JavaScript Language Features**
- **ESLint**
- **Prettier**
- **GitLens**
- **Docker**
- **PostgreSQL**
- **Thunder Client** (API testing)

### VS Code Settings

Create `.vscode/settings.json`:

```json
{
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": true
  },
  "typescript.preferences.importModuleSpecifier": "relative",
  "typescript.suggest.autoImports": true,
  "emmet.includeLanguages": {
    "typescript": "html",
    "typescriptreact": "html"
  }
}
```

### Browser Extensions

- **React Developer Tools**
- **Redux DevTools** (if using Redux)
- **JSON Formatter**

## 🚨 Common Issues

### Port Conflicts

If you get port conflicts:

```bash
# Check what's using the port
lsof -i :8000
lsof -i :3000

# Kill the process
kill -9 <PID>
```

### Database Connection Issues

```bash
# Check if PostgreSQL is running
brew services list | grep postgresql

# Start PostgreSQL
brew services start postgresql

# Check connection
psql -d lead_intelligence -c "SELECT 1;"
```

### Node Modules Issues

```bash
# Clear node modules and reinstall
rm -rf node_modules
rm -rf backend/node_modules
rm -rf frontend/node_modules
pnpm install
```

### TypeScript Errors

```bash
# Clear TypeScript cache
rm -rf backend/dist
rm -rf frontend/dist
pnpm type-check
```

## 📖 Additional Resources

### Documentation

- [Architecture Guide](./architecture.md)
- [API Documentation](./api.md)
- [Contributing Guidelines](./contributing.md)
- [Testing Guide](./testing.md)

### External Resources

- [React Documentation](https://react.dev/)
- [Node.js Documentation](https://nodejs.org/docs/)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

### Community

- [GitHub Issues](https://github.com/your-org/lead-intelligence-panel/issues)
- [GitHub Discussions](https://github.com/your-org/lead-intelligence-panel/discussions)
- [Discord Server](https://discord.gg/your-server)

---

Happy coding! 🚀 