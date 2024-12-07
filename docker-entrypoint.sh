#!/bin/bash
set -e

# Wait for Ollama to be ready
echo "Waiting for Ollama to start..."
until curl -s http://ollama:11434/api/tags > /dev/null; do
    echo "Waiting for Ollama service..."
    sleep 1
done

echo "Pulling Orca Mini model..."
curl -X POST http://ollama:11434/api/pull -d '{"name": "orca-mini"}'

echo "Waiting for model pull to complete..."
until curl -s http://ollama:11434/api/tags | grep -q "orca-mini"; do
    echo "Waiting for model to be ready..."
    sleep 5
done

# Start the application
echo "Starting RITA..."
exec python src/main.py