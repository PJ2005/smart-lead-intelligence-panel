# Contributing Guidelines

Thank you for your interest in contributing to the Lead Intelligence Panel! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### Types of Contributions

We welcome various types of contributions:

- **Bug Reports**: Report bugs and issues
- **Feature Requests**: Suggest new features
- **Code Contributions**: Submit pull requests
- **Documentation**: Improve or add documentation
- **Testing**: Write or improve tests
- **Design**: UI/UX improvements and suggestions

## 🚀 Getting Started

### Prerequisites

- Node.js 18+
- pnpm 8+
- PostgreSQL 14+
- Git

### Development Setup

1. **Fork the repository**
   ```bash
   git clone https://github.com/your-username/lead-intelligence-panel.git
   cd lead-intelligence-panel
   ```

2. **Install dependencies**
   ```bash
   pnpm install
   ```

3. **Set up environment**
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

## 📝 Code Style Guidelines

### General Principles

- **Readability**: Write code that is easy to read and understand
- **Consistency**: Follow established patterns and conventions
- **Documentation**: Document complex logic and APIs
- **Testing**: Write tests for new features and bug fixes

### TypeScript Guidelines

- Use strict TypeScript configuration
- Prefer interfaces over types for object shapes
- Use meaningful type names
- Avoid `any` type - use proper typing

```typescript
// Good
interface User {
  id: string;
  email: string;
  firstName: string;
  lastName: string;
}

// Avoid
type User = any;
```

### React Guidelines

- Use functional components with hooks
- Prefer composition over inheritance
- Use TypeScript for all components
- Follow React best practices

```typescript
// Good
interface ButtonProps {
  children: React.ReactNode;
  onClick: () => void;
  variant?: 'primary' | 'secondary';
}

const Button: React.FC<ButtonProps> = ({ 
  children, 
  onClick, 
  variant = 'primary' 
}) => {
  return (
    <button 
      className={`btn btn-${variant}`} 
      onClick={onClick}
    >
      {children}
    </button>
  );
};
```

### Backend Guidelines

- Use async/await for asynchronous operations
- Implement proper error handling
- Use dependency injection for services
- Follow RESTful API conventions

```typescript
// Good
class LeadService {
  constructor(
    private leadRepository: ILeadRepository,
    private emailService: IEmailService
  ) {}

  async createLead(leadData: CreateLeadDto): Promise<Lead> {
    try {
      const lead = await this.leadRepository.create(leadData);
      await this.emailService.sendNotification(lead);
      return lead;
    } catch (error) {
      throw new ApiError(400, 'Failed to create lead');
    }
  }
}
```

## 🔄 Git Workflow

### Branch Naming Convention

Use descriptive branch names with prefixes:

- `feature/` - New features
- `bugfix/` - Bug fixes
- `hotfix/` - Critical fixes
- `docs/` - Documentation updates
- `refactor/` - Code refactoring

Examples:
- `feature/user-authentication`
- `bugfix/lead-creation-error`
- `docs/api-documentation`

### Commit Message Convention

Follow conventional commits format:

```
type(scope): description

[optional body]

[optional footer]
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Test changes
- `chore`: Build/tooling changes

Examples:
```
feat(auth): add JWT authentication
fix(leads): resolve lead creation validation error
docs(api): update API documentation
```

### Pull Request Process

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Write code following style guidelines
   - Add tests for new functionality
   - Update documentation if needed

3. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat(scope): description"
   ```

4. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Create a pull request**
   - Use the PR template
   - Provide clear description
   - Link related issues

## 🧪 Testing Guidelines

### Test Structure

- **Unit Tests**: Test individual functions and components
- **Integration Tests**: Test API endpoints and database operations
- **E2E Tests**: Test complete user workflows

### Writing Tests

```typescript
// Unit test example
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

### Running Tests

```bash
# Run all tests
pnpm test

# Run specific test file
pnpm test -- src/services/leadService.test.ts

# Run tests with coverage
pnpm test:coverage

# Run tests in watch mode
pnpm test:watch
```

## 📚 Documentation Guidelines

### Code Documentation

- Use JSDoc for functions and classes
- Document complex algorithms
- Provide usage examples

```typescript
/**
 * Creates a new lead in the system
 * @param leadData - The lead data to create
 * @returns Promise resolving to the created lead
 * @throws {ApiError} When lead creation fails
 */
async createLead(leadData: CreateLeadDto): Promise<Lead> {
  // Implementation
}
```

### README Updates

- Update README files when adding new features
- Include setup instructions for new dependencies
- Document configuration changes

### API Documentation

- Update API documentation for new endpoints
- Include request/response examples
- Document error codes and messages

## 🔍 Code Review Process

### Review Checklist

Before submitting a PR, ensure:

- [ ] Code follows style guidelines
- [ ] Tests are written and passing
- [ ] Documentation is updated
- [ ] No console.log statements in production code
- [ ] Error handling is implemented
- [ ] Security considerations are addressed

### Review Guidelines

When reviewing code:

- Be constructive and respectful
- Focus on code quality and functionality
- Suggest improvements when possible
- Approve only when satisfied with changes

## 🐛 Bug Reports

### Bug Report Template

When reporting bugs, include:

1. **Description**: Clear description of the issue
2. **Steps to Reproduce**: Detailed steps to reproduce
3. **Expected Behavior**: What should happen
4. **Actual Behavior**: What actually happens
5. **Environment**: OS, browser, version information
6. **Screenshots**: If applicable

### Example Bug Report

```
**Bug Description**
The lead creation form doesn't validate email addresses properly.

**Steps to Reproduce**
1. Go to /leads/new
2. Enter an invalid email (e.g., "invalid-email")
3. Click "Create Lead"

**Expected Behavior**
Form should show validation error for invalid email.

**Actual Behavior**
Form submits successfully with invalid email.

**Environment**
- OS: macOS 12.0
- Browser: Chrome 96.0
- Version: 1.0.0
```

## 💡 Feature Requests

### Feature Request Template

When requesting features, include:

1. **Description**: Clear description of the feature
2. **Use Case**: Why this feature is needed
3. **Proposed Solution**: How you think it should work
4. **Alternatives**: Other approaches considered
5. **Mockups**: UI mockups if applicable

## 🚨 Security Issues

### Reporting Security Issues

For security issues:

1. **DO NOT** create a public issue
2. Email security@yourdomain.com
3. Include detailed description
4. Provide steps to reproduce
5. Wait for response before disclosure

## 🏷️ Issue Labels

We use the following labels:

- `bug`: Something isn't working
- `enhancement`: New feature or request
- `documentation`: Improvements to documentation
- `good first issue`: Good for newcomers
- `help wanted`: Extra attention is needed
- `priority: high`: High priority issues
- `priority: low`: Low priority issues

## 📋 Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No console.log statements
- [ ] Error handling implemented

## Related Issues
Closes #123
```

## 🎉 Recognition

### Contributors

We recognize contributors in several ways:

- **Contributors List**: Added to README.md
- **Release Notes**: Mentioned in release notes
- **Contributor Badge**: Special badge for significant contributions

### Contribution Levels

- **Bronze**: 1-5 contributions
- **Silver**: 6-15 contributions
- **Gold**: 16+ contributions
- **Platinum**: Core team member

## 📞 Getting Help

### Communication Channels

- **GitHub Issues**: For bugs and feature requests
- **GitHub Discussions**: For questions and discussions
- **Email**: For security issues

### Resources

- [Architecture Guide](./architecture.md)
- [API Documentation](./api.md)
- [Development Guide](./development.md)
- [Testing Guide](./testing.md)

## 📄 License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to the Lead Intelligence Panel! 🚀 