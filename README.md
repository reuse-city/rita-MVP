# RITA (Repair Intelligence Technical Assistant)

RITA is an AI-powered chat interface that helps people repair and maintain physical objects, part of the ThingData ecosystem. It combines multiple AI models to provide accessible repair guidance through text, image, and voice interfaces.

## Features

- 💬 LLM-powered repair assistance using Ollama/Llama2
- 🖼️ Object and damage detection with YOLOv8 (optional)
- 🎤 Voice interface with Whisper (optional)
- 🔧 Integration with ThingData repair knowledge base
- ⚡ Local-first architecture for privacy

## Quick Start

### Basic Setup (Chat Only)
```bash
# Clone repository
git clone https://github.com/reuse-city/rita.git
cd rita

# Start services
docker compose up -d

# Test the installation
curl http://localhost:8000/health
```

### Full Setup (Including Vision/Voice)
```bash
# Clone repository
git clone https://github.com/reuse-city/rita.git
cd rita

# Start with GPU support
docker compose -f docker-compose.yml -f docker-compose.gpu.yml up -d
```

See [Installation Guide](INSTALL.md) for detailed setup instructions.

## Project Structure
```
rita/
├── src/                      # Source code
│   ├── core/                 # Core business logic
│   │   ├── chat/            # Chat processing
│   │   ├── knowledge/       # Knowledge base integration
│   │   └── safety/         # Safety checks
│   ├── interfaces/          # External interfaces
│   │   ├── vision/         # Image processing
│   │   ├── voice/          # Voice processing
│   │   └── web/            # HTTP API
│   └── services/           # External integrations
│       ├── llm/            # Language models
│       ├── vision/         # Computer vision
│       └── voice/          # Speech processing
```

## Documentation

- [Installation Guide](INSTALL.md) - Detailed setup instructions
- [Architecture Overview](docs/architecture/overview.md) - System design
- [Development Guide](docs/setup/development.md) - Development setup
- [Testing Guide](TESTING.md) - Testing instructions
- [API Reference](docs/api/api-reference.md) - API documentation

## Contributing

1. Check [ROADMAP.md](ROADMAP.md) for planned features
2. Set up development environment following [development guide](docs/setup/development.md)
3. Run tests with `pytest`
4. Submit pull request

## License

GNU Affero General Public License v3.0 (AGPL-3.0)
