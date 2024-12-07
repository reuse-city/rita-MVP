# docs/setup/development.md
```markdown
# Development Guide

## Setup Development Environment

### Core Setup
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Optional Components
```bash
# Install vision/voice support
pip install -r requirements-extra.txt
```

## Configuration

### Development Configuration
1. Create development config:
```bash
cp config/default.yml config/development/config.yml
```

2. Edit as needed (example):
```yaml
app:
  name: RITA
  debug: true
  host: 0.0.0.0
  port: 8000

llm:
  base_url: http://ollama:11434
  model: llama2
```

## Development Workflow

### Running the Application
```bash
# Direct run
python src/main.py

# Or with uvicorn
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

### Code Style
- Use consistent indentation
- Add type hints
- Include docstrings
- Add comments for complex logic

### Testing
```bash
# Run tests
pytest

# Run with coverage
pytest --cov=src
```
```

