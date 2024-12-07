# Installation Guide

## Prerequisites

### Minimal Setup (Chat Only)
- Docker and Docker Compose
- 4GB RAM minimum
- 10GB disk space

### Full Setup (Vision/Voice)
- NVIDIA GPU with CUDA support
- 8GB RAM recommended
- 20GB disk space
- NVIDIA Container Toolkit

## Installation Methods

### 1. Docker Setup (Recommended)

#### Basic Installation
```bash
# Clone repository
git clone https://github.com/reuse-city/rita.git
cd rita

# Configure environment
cp config/default.yml config/development/config.yml
# Edit config/development/config.yml as needed

# Start services
docker compose up -d
```

#### GPU-Enabled Installation
```bash
# Clone repository
git clone https://github.com/reuse-city/rita.git
cd rita

# Configure environment
cp config/default.yml config/development/config.yml
# Edit config/development/config.yml as needed

# Start with GPU support
docker compose -f docker-compose.yml -f docker-compose.gpu.yml up -d
```

### 2. Manual Installation

```bash
# Clone repository
git clone https://github.com/reuse-city/rita.git
cd rita

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

# Install core dependencies
pip install -r requirements.txt

# Optional: Install vision/voice support
pip install -r requirements-extra.txt

# Configure environment
cp config/default.yml config/development/config.yml
# Edit config/development/config.yml

# Start service
python src/main.py
```

## Configuration

Configuration files are located in the `config/` directory:
- `default.yml`: Base configuration
- `development/`: Development environment configs
- `production/`: Production environment configs

## Verifying Installation

```bash
# Check health endpoint
curl http://localhost:8000/health

# Test chat endpoint
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello"}'
```

## Common Issues

### Memory Requirements
- Ensure sufficient memory for LLM model
- Monitor container memory usage
- See container logs for memory errors

### GPU Support
- Verify NVIDIA drivers installation
- Check NVIDIA Container Toolkit setup
- Monitor GPU memory usage

## Next Steps

- See [Development Guide](docs/setup/development.md) for development setup
- See [Model Setup](docs/setup/model-setup.md) for model configuration
- See [TESTING.md](TESTING.md) for testing instructions
