# docs/architecture/components.md
# RITA Components

## Core Components

### Chat Engine
- Manages conversation state
- Handles context tracking
- Processes user queries
- Formats responses
- Integrates safety checks

### Knowledge Management
- ThingData API client
- Query generation
- Result synthesis
- Caching layer
- Federation awareness

### Safety System
- Input validation
- Content filtering
- Warning generation
- Risk assessment
- Professional referral logic

## Service Integrations

### LLM Service
- Model: Llama2 via Ollama
- Context: 8192 tokens
- Temperature control
- Response formatting
- Safety prompts

### Vision Service
- Model: YOLOv8
- Object detection
- Damage assessment
- Image preprocessing
- Result confidence scoring

### Voice Service
- Model: Whisper
- Speech-to-text
- Language detection
- Noise handling
- Command recognition

# docs/setup/development.md
# Development Setup Guide

## Environment Setup

### 1. Basic Setup
```bash
# Clone repository
git clone https://github.com/reuse-city/rita.git
cd rita

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. GPU Setup (Optional)
```bash
# Install GPU dependencies
pip install -r requirements-extra.txt
```

## Configuration

### Development Configuration
1. Copy default configuration:
```bash
cp config/default.yml config/development/config.yml
```

2. Edit configuration:
```yaml
app:
  name: RITA
  debug: true
  host: 0.0.0.0
  port: 8000

llm:
  base_url: http://ollama:11434
  model: llama2

vision:
  enabled: true
  model: yolov8n.pt

voice:
  enabled: true
  model: base
```

## Development Workflow

### Running Services
```bash
# Start with basic setup
docker compose up -d

# Start with GPU support
docker compose -f docker-compose.yml -f docker-compose.gpu.yml up -d
```

### Code Style
- Use Black for formatting
- Use Ruff for linting
- Use type hints
- Follow FastAPI best practices

### Git Workflow
1. Create feature branch
2. Write tests
3. Implement feature
4. Run tests
5. Submit pull request

## Testing

### Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src
```

### Adding Tests
1. Unit tests in `tests/unit/`
2. Integration tests in `tests/integration/`
3. Update test documentation

## Documentation

### Building Docs
1. Update relevant .md files
2. Test examples
3. Update diagrams if needed

### API Documentation
FastAPI automatic documentation at:
- `/docs` - Swagger UI
- `/redoc` - ReDoc