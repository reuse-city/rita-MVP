# docs/setup/model-setup.md
```markdown
# Model Setup Guide

## LLM Setup (Required)

### Using Ollama
1. Ollama will automatically download required models
2. Default model: llama2
3. Configuration in development/config.yml:
```yaml
llm:
  base_url: http://ollama:11434
  model: llama2
```

## Vision Setup (Optional)

### YOLOv8 Setup
1. Install vision dependencies:
```bash
pip install -r requirements-extra.txt
```

2. Enable in configuration:
```yaml
vision:
  enabled: true
  model: yolov8n.pt
```

## Voice Setup (Optional)

### Whisper Setup
1. Install voice dependencies:
```bash
pip install -r requirements-extra.txt
```

2. Enable in configuration:
```yaml
voice:
  enabled: true
  model: base
```

## GPU Support

### Prerequisites
- NVIDIA GPU
- NVIDIA drivers
- NVIDIA Container Toolkit

### Configuration
Use GPU-enabled compose file:
```bash
docker compose -f docker-compose.yml -f docker-compose.gpu.yml up -d
```
```
