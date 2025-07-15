# Lead Intelligence Panel

A comprehensive, modular B2B lead intelligence platform designed to streamline lead management, analytics, and business intelligence for B2B organizations.

## 🚀 Overview

The Lead Intelligence Panel is a full-stack application that provides:
- **Lead Management**: Comprehensive lead tracking and lifecycle management
- **Intelligence Analytics**: Advanced analytics and insights for lead behavior
- **Business Intelligence**: Data-driven decision making tools
- **Modular Architecture**: Scalable, maintainable codebase with clear separation of concerns

## 🏗️ Architecture

### Backend (`/backend`)
- **API Layer**: RESTful and GraphQL APIs
- **Business Logic**: Core business services and domain logic
- **Data Layer**: Database models, repositories, and data access
- **Authentication**: JWT-based authentication and authorization
- **Real-time**: WebSocket support for live updates

### Frontend (`/frontend`)
- **React Application**: Modern, responsive UI
- **Component Library**: Reusable UI components
- **State Management**: Centralized state management
- **Routing**: Client-side routing with protected routes
- **Real-time Updates**: Live data synchronization

### Shared (`/shared`)
- **Types**: TypeScript interfaces and types
- **Utilities**: Common utilities and helpers
- **Constants**: Application-wide constants

## 📁 Project Structure

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

## 🛠️ Technology Stack

### Backend
- **Runtime**: Node.js with TypeScript
- **Framework**: Express.js or Fastify
- **Database**: PostgreSQL with Prisma ORM
- **Authentication**: JWT with bcrypt
- **Real-time**: Socket.io
- **Testing**: Jest with Supertest
- **Documentation**: Swagger/OpenAPI

### Frontend
- **Framework**: React 18 with TypeScript
- **Build Tool**: Vite
- **State Management**: Zustand or Redux Toolkit
- **UI Library**: Material-UI or Chakra UI
- **Routing**: React Router v6
- **Testing**: Vitest with React Testing Library
- **Styling**: CSS Modules or Styled Components

### DevOps & Tools
- **Package Manager**: pnpm
- **Linting**: ESLint + Prettier
- **Git Hooks**: Husky + lint-staged
- **Containerization**: Docker + Docker Compose
- **CI/CD**: GitHub Actions
- **Monitoring**: Sentry

## 🚀 Quick Start

### Prerequisites
- Node.js 18+ 
- pnpm 8+
- PostgreSQL 14+
- Docker (optional)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd lead-intelligence-panel
   ```

2. **Install dependencies**
   ```bash
   pnpm install
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. **Start development servers**
   ```bash
   # Start backend
   pnpm dev:backend
   
   # Start frontend (in another terminal)
   pnpm dev:frontend
   ```

5. **Access the application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

## 📚 Documentation

- [Architecture Guide](./docs/architecture.md)
- [API Documentation](./docs/api.md)
- [Development Guide](./docs/development.md)
- [Deployment Guide](./docs/deployment.md)
- [Contributing Guidelines](./docs/contributing.md)

## 🧪 Testing

```bash
# Run all tests
pnpm test

# Run backend tests
pnpm test:backend

# Run frontend tests
pnpm test:frontend

# Run tests with coverage
pnpm test:coverage
```

## 🏗️ Development

### Code Quality
- **Linting**: `pnpm lint`
- **Formatting**: `pnpm format`
- **Type Checking**: `pnpm type-check`

### Database
- **Migrations**: `pnpm db:migrate`
- **Seed Data**: `pnpm db:seed`
- **Reset**: `pnpm db:reset`

## 📦 Scripts

| Script | Description |
|--------|-------------|
| `pnpm dev` | Start both frontend and backend in development |
| `pnpm build` | Build both frontend and backend for production |
| `pnpm start` | Start production servers |
| `pnpm test` | Run all tests |
| `pnpm lint` | Run linting |
| `pnpm format` | Format code with Prettier |
| `pnpm docker:up` | Start Docker containers |
| `pnpm docker:down` | Stop Docker containers |

## 🤝 Contributing

Please read our [Contributing Guidelines](./docs/contributing.md) before submitting pull requests.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## 🆘 Support

- **Documentation**: Check the [docs](./docs/) directory
- **Issues**: Create an issue on GitHub
- **Discussions**: Use GitHub Discussions for questions

## 🔄 Version History

- **v1.0.0** - Initial project setup and structure
- **v0.1.0** - Project foundation and architecture

---

**Built with ❤️ for B2B lead intelligence** 