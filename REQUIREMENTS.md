# Requirements Documentation

## 📋 Overview

This document outlines all the system requirements, dependencies, and setup instructions for the **Vibe Coding Extended** FastAPI project. The project follows Python best practices and provides a modular, scalable architecture.

## 🎯 Project Information

- **Project Name**: Vibe Coding Extended API
- **Version**: 1.0.0
- **Python Version**: 3.11+
- **Framework**: FastAPI
- **Architecture**: Modular REST API with async support

## 🖥️ System Requirements

### Minimum System Requirements
- **Operating System**: macOS, Linux, or Windows
- **Python**: 3.11 or higher
- **RAM**: 512MB minimum (2GB recommended)
- **Storage**: 100MB for dependencies
- **Network**: Internet connection for dependency installation

### Recommended System Requirements
- **Operating System**: macOS 12+, Ubuntu 20.04+, or Windows 10+
- **Python**: 3.11 or 3.12
- **RAM**: 4GB or higher
- **Storage**: 1GB available space
- **CPU**: Multi-core processor
- **Network**: Stable broadband connection

## 🐍 Python Dependencies

### Core Production Dependencies

| Package | Version | Purpose | Documentation |
|---------|---------|---------|---------------|
| **fastapi** | 0.104.1 | Modern, fast web framework for building APIs | [FastAPI Docs](https://fastapi.tiangolo.com/) |
| **uvicorn[standard]** | 0.24.0 | ASGI server implementation with performance extras | [Uvicorn Docs](https://www.uvicorn.org/) |
| **pydantic** | 2.5.0 | Data validation using Python type hints | [Pydantic Docs](https://docs.pydantic.dev/) |
| **pydantic-settings** | 2.1.0 | Settings management with Pydantic | [Pydantic Settings](https://docs.pydantic.dev/latest/usage/settings/) |
| **gunicorn** | 21.2.0 | Python WSGI HTTP Server for UNIX (production) | [Gunicorn Docs](https://gunicorn.org/) |
| **httpx** | 0.25.2 | Async HTTP client library | [HTTPX Docs](https://www.python-httpx.org/) |
| **python-dotenv** | 1.0.0 | Environment variable management | [Python-dotenv](https://pypi.org/project/python-dotenv/) |

### Development Dependencies

| Package | Version | Purpose | Documentation |
|---------|---------|---------|---------------|
| **pytest** | 7.4.3 | Testing framework | [Pytest Docs](https://pytest.org/) |
| **pytest-asyncio** | 0.21.1 | Async support for pytest | [Pytest-asyncio](https://pytest-asyncio.readthedocs.io/) |
| **pytest-cov** | 4.1.0 | Coverage reporting for pytest | [Pytest-cov](https://pytest-cov.readthedocs.io/) |
| **black** | 23.11.0 | Code formatter | [Black Docs](https://black.readthedocs.io/) |
| **flake8** | 6.1.0 | Code linting and style checking | [Flake8 Docs](https://flake8.pycqa.org/) |
| **isort** | 5.12.0 | Import sorting | [isort Docs](https://pycqa.github.io/isort/) |
| **mypy** | 1.7.1 | Static type checking | [MyPy Docs](https://mypy.readthedocs.io/) |
| **watchdog** | 3.0.0 | File system event monitoring | [Watchdog](https://python-watchdog.readthedocs.io/) |
| **rich** | 13.7.0 | Rich text and beautiful formatting | [Rich Docs](https://rich.readthedocs.io/) |

### Future/Optional Dependencies (Currently Commented)

| Package | Version | Purpose | Status |
|---------|---------|---------|--------|
| **sqlalchemy** | 2.0.23 | Database ORM | Planned for database integration |
| **alembic** | 1.13.1 | Database migrations | Planned for database schema management |
| **python-jose[cryptography]** | 3.3.0 | JWT token handling | Planned for authentication |
| **passlib[bcrypt]** | 1.7.4 | Password hashing | Planned for user authentication |
| **python-multipart** | 0.0.6 | Form data parsing | Planned for file uploads |
| **mkdocs** | 1.5.3 | Documentation generator | Planned for enhanced documentation |
| **mkdocs-material** | 9.4.8 | Material theme for MkDocs | Planned for documentation styling |

## 🔧 Development Tools Configuration

### Code Quality Tools

#### Black (Code Formatting)
```toml
[tool.black]
line-length = 100
target-version = ['py311']
```

#### isort (Import Sorting)
```toml
[tool.isort]
profile = "black"
line_length = 100
multi_line_output = 3
```

#### MyPy (Type Checking)
```toml
[tool.mypy]
python_version = "3.11"
disallow_untyped_defs = true
strict_equality = true
```

#### Pytest (Testing)
```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-ra -q --strict-markers --strict-config"
```

## 🐳 Docker Requirements

### Docker Dependencies
- **Docker Engine**: 20.10+ or Docker Desktop
- **Docker Compose**: 2.0+ (included with Docker Desktop)

### Container Specifications
- **Base Image**: `python:3.11-slim`
- **Exposed Port**: 8000
- **Health Check**: Included with 30s intervals
- **User**: Non-root user for security

## 🌍 Environment Variables

### Required Environment Variables

| Variable | Type | Default | Description |
|----------|------|---------|-------------|
| `ENVIRONMENT` | string | `development` | Application environment (development/staging/production) |
| `DEBUG` | boolean | `true` | Enable debug mode |
| `SECRET_KEY` | string | *required* | Secret key for cryptographic operations |

### Optional Environment Variables

| Variable | Type | Default | Description |
|----------|------|---------|-------------|
| `DATABASE_URL` | string | `sqlite:///./vibe_coding.db` | Database connection string |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | integer | `30` | JWT token expiration time |
| `EXTERNAL_API_KEY` | string | `""` | External service API key |

## 🚀 Installation Requirements

### 1. System Prerequisites

**macOS:**
```bash
# Install Homebrew (if not already installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python 3.11
brew install python@3.11

# Verify installation
python3.11 --version
```

**Ubuntu/Debian:**
```bash
# Update package list
sudo apt update

# Install Python 3.11 and pip
sudo apt install python3.11 python3.11-venv python3.11-dev python3-pip

# Verify installation
python3.11 --version
```

**Windows:**
1. Download Python 3.11+ from [python.org](https://python.org)
2. Run installer with "Add Python to PATH" checked
3. Verify installation in Command Prompt: `python --version`

### 2. Virtual Environment Setup

```bash
# Create virtual environment
python3.11 -m venv venv

# Activate virtual environment
# macOS/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Upgrade pip
pip install --upgrade pip
```

### 3. Dependency Installation

**Production Dependencies:**
```bash
pip install -r requirements.txt
```

**Development Dependencies:**
```bash
pip install -r requirements-dev.txt
```

**Verify Installation:**
```bash
# Check FastAPI installation
python -c "import fastapi; print(f'FastAPI version: {fastapi.__version__}')"

# Check Uvicorn installation
uvicorn --version
```

## 🏗️ Build and Deployment Requirements

### Development Environment
- **Minimum**: Local Python 3.11+ with virtual environment
- **Recommended**: Docker Desktop for containerized development
- **IDE**: VS Code, PyCharm, or similar with Python support

### Testing Environment
- **Coverage Threshold**: 80% minimum
- **Test Runner**: pytest with async support
- **CI/CD**: GitHub Actions compatible

### Production Environment
- **Server**: Linux-based (Ubuntu 20.04+ recommended)
- **Python**: 3.11+ with production-ready ASGI server
- **Process Manager**: systemd or Docker containers
- **Reverse Proxy**: Nginx or Traefik (recommended)
- **Monitoring**: Health checks and logging configured

### Performance Requirements
- **Response Time**: < 200ms for health endpoints
- **Throughput**: 100+ requests/second (with proper deployment)
- **Memory Usage**: < 100MB for base application
- **Startup Time**: < 10 seconds

## 🔒 Security Requirements

### Development Security
- Environment variables for sensitive data
- No hardcoded secrets in code
- CORS configuration for frontend integration

### Production Security (Future)
- HTTPS/TLS encryption
- JWT-based authentication
- Input validation with Pydantic
- SQL injection prevention (with SQLAlchemy)
- Rate limiting middleware

## 📋 Compliance and Standards

### Code Quality Standards
- **PEP 8**: Python style guide compliance
- **Type Hints**: Full type annotation coverage
- **Documentation**: Docstrings for all public functions
- **Test Coverage**: Minimum 80% code coverage

### API Standards
- **REST**: RESTful API design principles
- **OpenAPI**: Automatic schema generation
- **Versioning**: API versioning support (/api/v1)
- **HTTP Status Codes**: Proper status code usage

## 🆘 Troubleshooting Requirements

### Common Issues and Solutions

1. **Port Already in Use (Error 48)**
   ```bash
   # Find process using port 8000
   lsof -i :8000
   # Kill process or use different port
   uvicorn app.main:app --reload --port 8001
   ```

2. **Unicode Encoding Error in Headers**
   - HTTP headers must use Latin-1 encoding
   - Avoid Unicode characters in header values
   - ✅ Fixed in current version

3. **Import Errors**
   ```bash
   # Ensure PYTHONPATH includes app directory
   export PYTHONPATH="${PYTHONPATH}:$(pwd)"
   ```

4. **Virtual Environment Issues**
   ```bash
   # Recreate virtual environment
   rm -rf venv
   python3.11 -m venv venv
   source venv/bin/activate
   pip install -r requirements-dev.txt
   ```

## 📞 Support and Resources

### Documentation Links
- **Project Repository**: https://github.com/faustocorreaa/vibe-coding-ex
- **FastAPI Documentation**: https://fastapi.tiangolo.com/
- **Python 3.11 Documentation**: https://docs.python.org/3.11/

### Development Resources
- **API Documentation**: http://localhost:8000/docs (when running)
- **Interactive API**: http://localhost:8000/redoc (when running)
- **Health Check**: http://localhost:8000/health

### Version Compatibility Matrix

| Python Version | FastAPI | Pydantic | Uvicorn | Status |
|----------------|---------|----------|---------|--------|
| 3.11.x | 0.104.1 | 2.5.0 | 0.24.0 | ✅ Supported |
| 3.12.x | 0.104.1 | 2.5.0 | 0.24.0 | ✅ Supported |
| 3.10.x | 0.104.1 | 2.5.0 | 0.24.0 | ⚠️ May work |
| 3.9.x | 0.104.1 | 2.5.0 | 0.24.0 | ❌ Not recommended |

---

## 📝 Notes

- This documentation is automatically generated based on the current project state
- All dependencies are pinned to specific versions for reproducibility
- Future features are marked as "planned" and dependencies are commented out
- Regular updates recommended as dependencies evolve

**Last Updated**: August 26, 2025  
**Document Version**: 1.0.0
