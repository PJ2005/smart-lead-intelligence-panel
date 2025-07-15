# Shared Module

The shared module contains common code, types, utilities, and constants that are used across both frontend and backend applications in the Lead Intelligence Panel.

## 🏗️ Purpose

This module serves as a single source of truth for:
- **Type Definitions**: Shared TypeScript interfaces and types
- **Utilities**: Common helper functions and utilities
- **Constants**: Application-wide constants and configurations
- **Validation Schemas**: Shared validation rules
- **Enums**: Common enumerations and constants

## 📁 Directory Structure

```
shared/
├── types/                 # TypeScript type definitions
│   ├── api.ts            # API request/response types
│   ├── entities.ts       # Database entity types
│   ├── common.ts         # Common utility types
│   └── index.ts          # Type exports
├── utils/                 # Utility functions
│   ├── validation.ts     # Validation utilities
│   ├── formatting.ts     # Data formatting utilities
│   ├── dateUtils.ts      # Date manipulation utilities
│   ├── encryption.ts     # Encryption utilities
│   └── index.ts          # Utility exports
├── constants/             # Application constants
│   ├── api.ts            # API-related constants
│   ├── business.ts       # Business logic constants
│   ├── validation.ts     # Validation constants
│   └── index.ts          # Constant exports
├── schemas/               # Validation schemas
│   ├── user.ts           # User validation schemas
│   ├── lead.ts           # Lead validation schemas
│   ├── company.ts        # Company validation schemas
│   └── index.ts          # Schema exports
├── enums/                 # Enumerations
│   ├── userRoles.ts      # User role enumerations
│   ├── leadStatus.ts     # Lead status enumerations
│   ├── activityTypes.ts  # Activity type enumerations
│   └── index.ts          # Enum exports
├── package.json           # Package configuration
└── tsconfig.json          # TypeScript configuration
```

## 🚀 Usage

### Installation

The shared module is automatically available to both frontend and backend through workspace dependencies.

### Importing Types

```typescript
// In frontend or backend
import { User, Lead, ApiResponse } from '@shared/types';
import { validateEmail, formatCurrency } from '@shared/utils';
import { API_ENDPOINTS, USER_ROLES } from '@shared/constants';
```

## 📋 Type Definitions

### API Types

```typescript
// api.ts
export interface ApiResponse<T = any> {
  success: boolean;
  data?: T;
  error?: string;
  message?: string;
}

export interface PaginatedResponse<T> extends ApiResponse<T[]> {
  pagination: {
    page: number;
    limit: number;
    total: number;
    totalPages: number;
  };
}

export interface ApiError {
  code: string;
  message: string;
  details?: any;
}
```

### Entity Types

```typescript
// entities.ts
export interface User {
  id: string;
  email: string;
  firstName: string;
  lastName: string;
  role: UserRole;
  companyId?: string;
  createdAt: Date;
  updatedAt: Date;
}

export interface Lead {
  id: string;
  firstName: string;
  lastName: string;
  email: string;
  phone?: string;
  company: string;
  status: LeadStatus;
  source: string;
  assignedTo?: string;
  createdAt: Date;
  updatedAt: Date;
}

export interface Company {
  id: string;
  name: string;
  industry: string;
  size: CompanySize;
  website?: string;
  createdAt: Date;
  updatedAt: Date;
}
```

## 🛠️ Utilities

### Validation Utilities

```typescript
// validation.ts
export const validateEmail = (email: string): boolean => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
};

export const validatePhone = (phone: string): boolean => {
  const phoneRegex = /^\+?[\d\s\-\(\)]+$/;
  return phoneRegex.test(phone);
};

export const validatePassword = (password: string): boolean => {
  return password.length >= 8 && 
         /[A-Z]/.test(password) && 
         /[a-z]/.test(password) && 
         /\d/.test(password);
};
```

### Formatting Utilities

```typescript
// formatting.ts
export const formatCurrency = (amount: number, currency = 'USD'): string => {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency,
  }).format(amount);
};

export const formatDate = (date: Date, format = 'short'): string => {
  const options: Intl.DateTimeFormatOptions = {
    short: { year: 'numeric', month: 'short', day: 'numeric' },
    long: { year: 'numeric', month: 'long', day: 'numeric' },
    time: { hour: '2-digit', minute: '2-digit' },
  };
  
  return new Intl.DateTimeFormat('en-US', options[format]).format(date);
};

export const formatPhoneNumber = (phone: string): string => {
  const cleaned = phone.replace(/\D/g, '');
  const match = cleaned.match(/^(\d{3})(\d{3})(\d{4})$/);
  return match ? `(${match[1]}) ${match[2]}-${match[3]}` : phone;
};
```

### Date Utilities

```typescript
// dateUtils.ts
export const addDays = (date: Date, days: number): Date => {
  const result = new Date(date);
  result.setDate(result.getDate() + days);
  return result;
};

export const getDaysBetween = (startDate: Date, endDate: Date): number => {
  const timeDiff = endDate.getTime() - startDate.getTime();
  return Math.ceil(timeDiff / (1000 * 3600 * 24));
};

export const isToday = (date: Date): boolean => {
  const today = new Date();
  return date.toDateString() === today.toDateString();
};

export const isThisWeek = (date: Date): boolean => {
  const today = new Date();
  const weekStart = new Date(today.setDate(today.getDate() - today.getDay()));
  const weekEnd = new Date(weekStart);
  weekEnd.setDate(weekEnd.getDate() + 6);
  
  return date >= weekStart && date <= weekEnd;
};
```

## 📊 Constants

### API Constants

```typescript
// api.ts
export const API_ENDPOINTS = {
  AUTH: {
    LOGIN: '/auth/login',
    LOGOUT: '/auth/logout',
    REFRESH: '/auth/refresh',
    REGISTER: '/auth/register',
  },
  LEADS: {
    LIST: '/leads',
    CREATE: '/leads',
    UPDATE: '/leads/:id',
    DELETE: '/leads/:id',
    ANALYTICS: '/leads/analytics',
  },
  USERS: {
    LIST: '/users',
    PROFILE: '/users/profile',
    UPDATE: '/users/:id',
  },
} as const;

export const HTTP_STATUS = {
  OK: 200,
  CREATED: 201,
  BAD_REQUEST: 400,
  UNAUTHORIZED: 401,
  FORBIDDEN: 403,
  NOT_FOUND: 404,
  INTERNAL_SERVER_ERROR: 500,
} as const;
```

### Business Constants

```typescript
// business.ts
export const LEAD_SOURCES = [
  'WEBSITE',
  'SOCIAL_MEDIA',
  'EMAIL_CAMPAIGN',
  'REFERRAL',
  'COLD_CALL',
  'TRADE_SHOW',
  'OTHER',
] as const;

export const COMPANY_SIZES = [
  'STARTUP',
  'SMALL',
  'MEDIUM',
  'LARGE',
  'ENTERPRISE',
] as const;

export const INDUSTRIES = [
  'TECHNOLOGY',
  'HEALTHCARE',
  'FINANCE',
  'EDUCATION',
  'RETAIL',
  'MANUFACTURING',
  'CONSULTING',
  'OTHER',
] as const;
```

### Validation Constants

```typescript
// validation.ts
export const VALIDATION_RULES = {
  EMAIL: {
    MIN_LENGTH: 5,
    MAX_LENGTH: 254,
    PATTERN: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
  },
  PASSWORD: {
    MIN_LENGTH: 8,
    MAX_LENGTH: 128,
    REQUIRE_UPPERCASE: true,
    REQUIRE_LOWERCASE: true,
    REQUIRE_NUMBERS: true,
    REQUIRE_SPECIAL_CHARS: false,
  },
  NAME: {
    MIN_LENGTH: 2,
    MAX_LENGTH: 50,
    PATTERN: /^[a-zA-Z\s\-']+$/,
  },
  PHONE: {
    MIN_LENGTH: 10,
    MAX_LENGTH: 15,
    PATTERN: /^\+?[\d\s\-\(\)]+$/,
  },
} as const;
```

## 🔧 Enumerations

### User Roles

```typescript
// userRoles.ts
export enum UserRole {
  ADMIN = 'ADMIN',
  MANAGER = 'MANAGER',
  SALES_REP = 'SALES_REP',
  ANALYST = 'ANALYST',
  VIEWER = 'VIEWER',
}

export const USER_ROLE_LABELS: Record<UserRole, string> = {
  [UserRole.ADMIN]: 'Administrator',
  [UserRole.MANAGER]: 'Manager',
  [UserRole.SALES_REP]: 'Sales Representative',
  [UserRole.ANALYST]: 'Analyst',
  [UserRole.VIEWER]: 'Viewer',
};
```

### Lead Status

```typescript
// leadStatus.ts
export enum LeadStatus {
  NEW = 'NEW',
  CONTACTED = 'CONTACTED',
  QUALIFIED = 'QUALIFIED',
  PROPOSAL = 'PROPOSAL',
  NEGOTIATION = 'NEGOTIATION',
  CLOSED_WON = 'CLOSED_WON',
  CLOSED_LOST = 'CLOSED_LOST',
}

export const LEAD_STATUS_LABELS: Record<LeadStatus, string> = {
  [LeadStatus.NEW]: 'New',
  [LeadStatus.CONTACTED]: 'Contacted',
  [LeadStatus.QUALIFIED]: 'Qualified',
  [LeadStatus.PROPOSAL]: 'Proposal',
  [LeadStatus.NEGOTIATION]: 'Negotiation',
  [LeadStatus.CLOSED_WON]: 'Closed Won',
  [LeadStatus.CLOSED_LOST]: 'Closed Lost',
};
```

## 📋 Validation Schemas

### User Schema

```typescript
// user.ts
import { z } from 'zod';

export const userSchema = z.object({
  email: z.string().email(),
  firstName: z.string().min(2).max(50),
  lastName: z.string().min(2).max(50),
  role: z.enum(['ADMIN', 'MANAGER', 'SALES_REP', 'ANALYST', 'VIEWER']),
  companyId: z.string().optional(),
});

export const userUpdateSchema = userSchema.partial();
```

### Lead Schema

```typescript
// lead.ts
import { z } from 'zod';

export const leadSchema = z.object({
  firstName: z.string().min(2).max(50),
  lastName: z.string().min(2).max(50),
  email: z.string().email(),
  phone: z.string().optional(),
  company: z.string().min(2).max(100),
  status: z.enum(['NEW', 'CONTACTED', 'QUALIFIED', 'PROPOSAL', 'NEGOTIATION', 'CLOSED_WON', 'CLOSED_LOST']),
  source: z.string().min(2).max(50),
  assignedTo: z.string().optional(),
});

export const leadUpdateSchema = leadSchema.partial();
```

## 🚀 Development

### Adding New Types

1. Create the type definition in the appropriate file
2. Export it from the file's index
3. Update the main types index file
4. Add JSDoc comments for documentation

### Adding New Utilities

1. Create the utility function with proper TypeScript types
2. Add comprehensive JSDoc documentation
3. Include unit tests for the utility
4. Export from the utils index file

### Adding New Constants

1. Define constants with clear, descriptive names
2. Use `as const` for type safety
3. Group related constants together
4. Export from the constants index file

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pnpm test

# Run specific test file
pnpm test -- utils/validation.test.ts

# Run tests with coverage
pnpm test:coverage
```

### Test Structure

- **Unit Tests**: Test individual functions and utilities
- **Type Tests**: Ensure type definitions work correctly
- **Integration Tests**: Test utility combinations

## 📚 Documentation

- **JSDoc**: Comprehensive documentation for all functions
- **TypeScript**: Self-documenting types
- **Examples**: Usage examples in documentation
- **Changelog**: Track changes to shared utilities

## 🤝 Contributing

1. Follow TypeScript best practices
2. Write comprehensive tests
3. Add JSDoc documentation
4. Ensure backward compatibility
5. Update the changelog

## 📄 License

This module is part of the Lead Intelligence Panel project and follows the same license terms. 