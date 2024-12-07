# tests/unit/test_config.py
import pytest
import os
from src.config import Config

def test_default_config_load():
    """Test loading default configuration."""
    config = Config.load()
    
    # Test basic config structure
    assert config.app.name == "RITA"
    assert config.llm.service == "ollama"
    assert isinstance(config.llm.timeout, int)
    
def test_environment_specific_config():
    """Test loading environment-specific configuration."""
    # Set environment to development
    os.environ['RITA_ENV'] = 'development'
    config = Config.load()
    
    # Development should have debug enabled
    assert config.app.debug is True
    
def test_config_deep_merge():
    """Test that environment configs properly override defaults."""
    os.environ['RITA_ENV'] = 'development'
    config = Config.load()
    
    # Check that default values remain when not overridden
    assert config.app.name == "RITA"  # from default config
    assert config.llm.timeout == 60    # from development config

def test_invalid_environment():
    """Test behavior with invalid environment."""
    os.environ['RITA_ENV'] = 'nonexistent'
    config = Config.load()
    
    # Should fall back to default values
    assert config.app.name == "RITA"
    assert isinstance(config.app.port, int)

def test_required_config_fields():
    """Test that all required configuration fields are present."""
    config = Config.load()
    
    # Test presence of all required sections
    assert config.app is not None
    assert config.llm is not None
    assert config.vision is not None
    assert config.voice is not None
    assert config.safety is not None