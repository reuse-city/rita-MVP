# docs/setup/installation.md
```markdown
# RITA Installation Guide

## Installation Methods

### 1. Docker Installation (Recommended)

#### Prerequisites
- Docker
- Docker Compose
- Git

#### Basic Installation
```bash
# Clone repository
git clone https://github.com/reuse-city/rita.git
cd rita

# Configure
cp config/default.yml config/development/config.yml
# Edit config as needed

# Start services
docker compose up -d
```

#### GPU-enabled Installation
Additional prerequisites:
- NVIDIA GPU
- NVIDIA Container Toolkit

```bash
# Start with GPU support
docker compose -f docker-compose.yml -f docker-compose.gpu.yml up -d
```

### 2. Manual Installation

#### Prerequisites
- Python 3.9+
- pip
- virtualenv

#### Steps
```bash
# Clone repository
git clone https://github.com/reuse-city/rita.git
cd rita

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Optional: Install vision/voice support
pip install -r requirements-extra.txt

# Start service
python src/main.py
```

## Verifying Installation

```bash
# Check health endpoint
curl http://localhost:8000/health

# Test chat endpoint
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello"}'
```
```

