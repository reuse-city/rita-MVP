# Testing Guide

## Test Structure

```
tests/
├── integration/           # Integration tests
│   └── [pending]        # Integration test files
└── unit/               # Unit tests
    └── test_config.py  # Configuration tests
```

## Running Tests

### Basic Test Run
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/unit/test_config.py

# Run with verbose output
pytest -v
```

### Test Configuration

Configuration is managed through `pytest.ini`:
```ini
[pytest]
asyncio_mode = auto
testpaths = tests
python_files = test_*.py
```

## Development Environment

### Installing Test Dependencies
Test dependencies are included in core requirements:
```bash
pip install -r requirements.txt
```

### Running Tests in Docker
```bash
# Run tests in container
docker compose run --rm rita pytest

# Run specific test file
docker compose run --rm rita pytest tests/unit/test_config.py
```

## Adding Tests

### Unit Tests
Place in `tests/unit/`:
```python
# test_example.py
def test_feature():
    assert True
```

### Integration Tests
Place in `tests/integration/`:
```python
# test_api.py
async def test_health_endpoint(client):
    response = await client.get("/health")
    assert response.status_code == 200
```

## Test Coverage

Coverage reporting:
```bash
# Run tests with coverage
pytest --cov=src

# Generate HTML report
pytest --cov=src --cov-report=html
```

## Continuous Integration

Tests are run automatically on:
- Pull requests
- Pushes to main branch
- Manual trigger

## Future Improvements

Planned test additions:
1. Integration tests for all endpoints
2. Vision service tests
3. Voice service tests
4. Performance tests
5. Security tests

See [ROADMAP.md](ROADMAP.md) for more details.
