# docker-entrypoint.sh
#!/bin/bash
set -e

# Start Ollama in the background
ollama serve &

# Wait for Ollama to be ready
echo "Waiting for Ollama to start..."
until curl -s http://localhost:11434/api/tags > /dev/null; do
    sleep 1
done

# Pull the required model
echo "Pulling Llama 2 model..."
ollama pull llama2

# Start the application
echo "Starting RITA..."
exec python src/main.py