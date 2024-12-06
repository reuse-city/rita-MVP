# RITA (Repair Intelligence Technical Assistant)

RITA is an open-source AI assistant designed to help people repair and maintain physical objects. It combines conversational AI with computer vision and voice recognition to provide accessible repair guidance.

## Core Features

- 🤖 AI-powered repair assistance using open source models
- 🖼️ Image recognition for object and damage identification
- 🎤 Voice interface for hands-free operation
- 🔧 Integration with repair knowledge databases
- ⚡ Local-first architecture for privacy and independence

## Technology Stack

- **LLM**: Llama 2 via Ollama
- **Image Recognition**: YOLOv8
- **Voice Recognition**: Whisper
- **Backend**: FastAPI
- **Frontend**: React with Tailwind CSS

# Development Setup Guide

## Prerequisites
- Python 3.9+
- Docker and Docker Compose
- Git

## Initial Setup

1. Clone the repository:
```bash
git clone https://github.com/reuse-city/rita-MVP.git
cd rita-MVP
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up configuration:
```bash
cp config/default.yml config/development.yml
# Edit development.yml as needed
```

## Running the Application

### Using Docker
```bash
docker-compose up --build
```

### Local Development
```bash
# Start Ollama service separately
ollama serve

# Pull required model
ollama pull llama2

# Start the application
python src/main.py
```

## Project Structure

```
rita-MVP/
├── src/                 # Source code
│   ├── core/           # Core business logic
│   │   ├── chat/       # Chat processing
│   │   ├── knowledge/  # Knowledge management
│   │   └── safety/     # Safety checks
│   ├── interfaces/     # External interfaces
│   │   ├── web/       # Web API
│   │   ├── vision/    # Image processing
│   │   └── voice/     # Voice interface
│   ├── services/      # External service integrations
│   │   ├── llm/       # LLM service
│   │   ├── vision/    # Vision service
│   │   └── voice/     # Voice service
│   └── models/        # Data models
├── config/            # Configuration files
├── tests/             # Test suite
└── docs/              # Documentation

Current Implementation Status:
- ✅ Basic FastAPI application
- ✅ LLM service integration
- ✅ Configuration management
- ✅ Docker setup
- 🔄 Documentation
- ⏳ Testing
```

## Configuration

The application uses YAML configuration files located in the `config/` directory:
- `default.yml`: Default configuration template
- `development.yml`: Development environment settings
- `production.yml`: Production environment settings

## Testing

Run tests using pytest:
```bash
pytest tests/
```

## Contributing

1. Create a feature branch:
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes and commit:
```bash
git add .
git commit -m "Description of changes"
```

3. Push changes and create a pull request:
```bash
git push origin feature/your-feature-name
```

## License

This project is licensed under the GNU Affero General Public License v3.0 (AGPL-3.0).

## Acknowledgments

RITA is part of the ThingData ecosystem, developed to promote longer lifetime for goods and materials through repair and maintenance.
