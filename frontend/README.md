# Frontend Module

The frontend module provides a modern, responsive React application for the Lead Intelligence Panel with real-time updates and comprehensive analytics dashboards.

## 🏗️ Architecture

### Core Components

- **Components** (`src/components/`): Reusable UI components
- **Pages** (`src/pages/`): Page-level components and routing
- **Hooks** (`src/hooks/`): Custom React hooks
- **Services** (`src/services/`): API service layer
- **Store** (`src/store/`): State management
- **Utils** (`src/utils/`): Utility functions
- **Types** (`src/types/`): TypeScript type definitions

### Key Features

- **Modern React**: React 18 with hooks and functional components
- **TypeScript**: Full type safety and IntelliSense support
- **Responsive Design**: Mobile-first responsive design
- **Real-time Updates**: WebSocket integration for live data
- **State Management**: Centralized state with Zustand
- **Routing**: Client-side routing with React Router
- **Component Library**: Reusable UI component system
- **Theme System**: Customizable design system

## 🚀 Quick Start

### Prerequisites
- Node.js 18+
- pnpm 8+

### Installation

1. **Install dependencies**
   ```bash
   cd frontend
   pnpm install
   ```

2. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Configure your environment variables
   ```

3. **Start development server**
   ```bash
   pnpm dev
   ```

4. **Access the application**
   - Development: http://localhost:3000
   - Build preview: http://localhost:4173

## 📁 Directory Structure

```
frontend/
├── src/
│   ├── components/         # Reusable UI components
│   │   ├── common/        # Common UI components
│   │   │   ├── Button/    # Button component
│   │   │   ├── Input/     # Input component
│   │   │   ├── Modal/     # Modal component
│   │   │   └── Table/     # Table component
│   │   ├── layout/        # Layout components
│   │   │   ├── Header/    # Header component
│   │   │   ├── Sidebar/   # Sidebar navigation
│   │   │   └── Footer/    # Footer component
│   │   ├── forms/         # Form components
│   │   │   ├── LeadForm/  # Lead creation/editing form
│   │   │   └── AuthForm/  # Authentication forms
│   │   └── charts/        # Chart and visualization components
│   │       ├── LineChart/ # Line chart component
│   │       ├── BarChart/  # Bar chart component
│   │       └── PieChart/  # Pie chart component
│   ├── pages/             # Page components
│   │   ├── Dashboard/     # Main dashboard page
│   │   ├── Leads/         # Lead management pages
│   │   ├── Analytics/     # Analytics pages
│   │   ├── Settings/      # Settings pages
│   │   └── Auth/          # Authentication pages
│   ├── hooks/             # Custom React hooks
│   │   ├── useAuth.ts     # Authentication hook
│   │   ├── useLeads.ts    # Lead data hook
│   │   ├── useWebSocket.ts # WebSocket hook
│   │   └── useLocalStorage.ts # Local storage hook
│   ├── services/          # API service layer
│   │   ├── api.ts         # Base API configuration
│   │   ├── authService.ts # Authentication service
│   │   ├── leadService.ts # Lead management service
│   │   ├── analyticsService.ts # Analytics service
│   │   └── websocketService.ts # WebSocket service
│   ├── store/             # State management
│   │   ├── authStore.ts   # Authentication state
│   │   ├── leadStore.ts   # Lead data state
│   │   ├── uiStore.ts     # UI state
│   │   └── index.ts       # Store configuration
│   ├── utils/             # Utility functions
│   │   ├── validation.ts  # Form validation
│   │   ├── formatting.ts  # Data formatting
│   │   ├── constants.ts   # Application constants
│   │   └── helpers.ts     # Helper functions
│   ├── types/             # TypeScript types
│   │   ├── api.ts         # API response types
│   │   ├── components.ts  # Component prop types
│   │   └── common.ts      # Common types
│   ├── styles/            # Global styles
│   │   ├── globals.css    # Global CSS
│   │   ├── variables.css  # CSS variables
│   │   └── components.css # Component styles
│   ├── App.tsx            # Main App component
│   ├── main.tsx           # Application entry point
│   └── vite-env.d.ts      # Vite type definitions
├── public/                # Static assets
│   ├── images/           # Image assets
│   ├── icons/            # Icon assets
│   └── favicon.ico       # Favicon
├── docs/                 # Frontend documentation
│   ├── components.md     # Component documentation
│   ├── styling.md        # Styling guide
│   └── deployment.md     # Deployment guide
├── package.json          # Dependencies and scripts
├── vite.config.ts        # Vite configuration
├── tsconfig.json         # TypeScript configuration
└── tailwind.config.js    # Tailwind CSS configuration
```

## 🛠️ Development

### Available Scripts

| Script | Description |
|--------|-------------|
| `pnpm dev` | Start development server with hot reload |
| `pnpm build` | Build for production |
| `pnpm preview` | Preview production build |
| `pnpm test` | Run all tests |
| `pnpm test:watch` | Run tests in watch mode |
| `pnpm test:coverage` | Run tests with coverage |
| `pnpm lint` | Run ESLint |
| `pnpm format` | Format code with Prettier |
| `pnpm type-check` | Run TypeScript type checking |

### Code Quality

- **TypeScript**: Strict type checking enabled
- **ESLint**: Code linting with React-specific rules
- **Prettier**: Code formatting
- **Husky**: Git hooks for pre-commit checks
- **Vitest**: Fast unit testing with React Testing Library

### Component Development

- **Storybook**: Component development and documentation
- **Component Testing**: Unit tests for all components
- **Accessibility**: ARIA compliance and keyboard navigation
- **Responsive Design**: Mobile-first approach

## 🔧 Configuration

### Environment Variables

```env
# API Configuration
VITE_API_URL=http://localhost:8000
VITE_WS_URL=ws://localhost:8000

# Authentication
VITE_AUTH_DOMAIN=your-auth-domain
VITE_AUTH_CLIENT_ID=your-client-id

# External Services
VITE_GOOGLE_ANALYTICS_ID=your-ga-id
VITE_SENTRY_DSN=your-sentry-dsn

# Feature Flags
VITE_ENABLE_ANALYTICS=true
VITE_ENABLE_REAL_TIME=true
```

### Build Configuration

- **Vite**: Fast build tool with HMR
- **TypeScript**: Strict type checking
- **Tailwind CSS**: Utility-first CSS framework
- **PostCSS**: CSS processing and optimization

## 📚 Component Documentation

### Component Structure

Each component follows a consistent structure:

```
ComponentName/
├── index.tsx          # Main component file
├── ComponentName.tsx  # Component implementation
├── ComponentName.test.tsx # Component tests
├── ComponentName.stories.tsx # Storybook stories
└── ComponentName.module.css # Component styles (if needed)
```

### Component Guidelines

- **Functional Components**: Use hooks and functional components
- **TypeScript**: Full type safety for props and state
- **Props Interface**: Define clear prop interfaces
- **Default Props**: Provide sensible defaults
- **Error Boundaries**: Handle component errors gracefully

## 🧪 Testing

### Test Structure

- **Unit Tests**: Test individual components and functions
- **Integration Tests**: Test component interactions
- **E2E Tests**: Test complete user workflows

### Testing Tools

- **Vitest**: Fast test runner
- **React Testing Library**: Component testing utilities
- **MSW**: API mocking for tests
- **Jest DOM**: DOM testing utilities

### Running Tests

```bash
# Run all tests
pnpm test

# Run specific test file
pnpm test -- src/components/Button/Button.test.tsx

# Run tests with coverage
pnpm test:coverage

# Run tests in watch mode
pnpm test:watch
```

## 🎨 Styling

### Design System

- **Tailwind CSS**: Utility-first CSS framework
- **CSS Variables**: Custom properties for theming
- **Component Library**: Consistent design patterns
- **Responsive Design**: Mobile-first approach

### Theme Configuration

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#eff6ff',
          500: '#3b82f6',
          900: '#1e3a8a',
        },
        // ... other custom colors
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
      },
    },
  },
}
```

## 🔒 Security

- **Input Validation**: Client-side form validation
- **XSS Prevention**: Sanitized user inputs
- **CSRF Protection**: Token-based CSRF protection
- **Content Security Policy**: CSP headers
- **Secure Headers**: Security-focused HTTP headers

## 📊 Performance

- **Code Splitting**: Route-based code splitting
- **Lazy Loading**: Component lazy loading
- **Image Optimization**: Optimized image loading
- **Caching**: Browser caching strategies
- **Bundle Analysis**: Webpack bundle analyzer

## 🚀 Deployment

### Production Build

```bash
# Build the application
pnpm build

# Preview production build
pnpm preview
```

### Docker Deployment

```bash
# Build Docker image
docker build -t lead-intelligence-frontend .

# Run container
docker run -p 3000:3000 lead-intelligence-frontend
```

### Static Hosting

The application can be deployed to:
- **Vercel**: Zero-config deployment
- **Netlify**: Static site hosting
- **AWS S3**: Static website hosting
- **GitHub Pages**: Free static hosting

## 🤝 Contributing

1. Follow the component development guidelines
2. Write tests for new components
3. Update Storybook stories
4. Ensure accessibility compliance
5. Use conventional commits for commit messages

## 📄 License

This module is part of the Lead Intelligence Panel project and follows the same license terms. 