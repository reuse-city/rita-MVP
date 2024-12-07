# scripts/cleanup.sh
#!/bin/bash

echo "🧹 Cleaning up RITA..."

# Stop and remove containers
echo "Stopping containers..."
docker-compose down

# Remove Docker images
echo "Removing Docker images..."
docker rmi rita-mvp-rita

# Remove Python cache files
echo "Removing Python cache..."
find . -type d -name "__pycache__" -exec rm -r {} +
find . -type f -name "*.pyc" -delete

# Remove virtual environment
echo "Removing virtual environment..."
rm -rf venv/

# Remove logs
echo "Removing logs..."
rm -rf logs/

# Remove local config files but preserve examples
echo "Removing local config files..."
find ./config -name "config.yml" -not -name "default.yml" -delete

echo "✨ Cleanup complete! To restart fresh:"
echo "1. python -m venv venv"
echo "2. source venv/bin/activate"
echo "3. pip install -r requirements.txt"
echo "4. docker-compose up --build"