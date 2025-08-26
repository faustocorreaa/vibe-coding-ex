# Vibe Coding Extended - FastAPI Edition ✨

An extended version of vibe-coding built with FastAPI, following Python best practices.

## 🚀 Features

- FastAPI backend with async support
- Structured project layout
- Environment configuration
- API documentation with Swagger UI
- Docker support
- Testing framework
- Linting and formatting tools

## 📁 Project Structure

```
vibe-coding-ex/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app entry point
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py        # Configuration settings
│   │   └── dependencies.py  # Dependency injection
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   └── greetings.py # Greeting endpoints
│   │   └── middleware.py    # Custom middleware
│   ├── models/
│   │   └── __init__.py
│   ├── services/
│   │   └── __init__.py
│   └── utils/
│       └── __init__.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── requirements.txt
├── requirements-dev.txt
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── .gitignore
└── pyproject.toml
```

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/faustocorreaa/vibe-coding-ex.git
cd vibe-coding-ex
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Copy environment variables:
```bash
cp .env.example .env
```

## 🚀 Running the Application

### Development Mode
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Using Docker
```bash
docker-compose up --build
```

## 📚 API Documentation

Once the server is running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🧪 Testing

```bash
pytest tests/ -v
```

## 🎯 API Endpoints

- `GET /` - Health check
- `GET /hello` - Simple greeting
- `GET /hello/{name}` - Personalized greeting

## 🛠️ Development Tools

- **FastAPI**: Modern, fast web framework
- **Uvicorn**: ASGI server
- **Pydantic**: Data validation
- **Pytest**: Testing framework
- **Black**: Code formatting
- **Flake8**: Code linting
- **Docker**: Containerization

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and linting
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

---

*Built with ❤️ and good vibes! ✨*