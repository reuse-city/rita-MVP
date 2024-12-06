# src/config.py
import os
import yaml
from typing import Optional, Dict, Any
from pydantic import BaseModel

class AppConfig(BaseModel):
    name: str
    host: str
    port: int
    debug: bool

class LLMConfig(BaseModel):
    service: str
    base_url: str
    model: str
    timeout: int

class VisionConfig(BaseModel):
    enabled: bool
    model: str
    confidence_threshold: float

class VoiceConfig(BaseModel):
    enabled: bool
    model: str
    language: str

class SafetyConfig(BaseModel):
    max_requests_per_minute: int
    require_safety_warnings: bool

class Config(BaseModel):
    app: AppConfig
    llm: LLMConfig
    vision: VisionConfig
    voice: VoiceConfig
    safety: SafetyConfig

    @classmethod
    def load(cls, env: Optional[str] = None) -> 'Config':
        # Determine environment
        env = env or os.getenv('RITA_ENV', 'development')
        
        # Load default config
        with open('config/default.yml', 'r') as f:
            config_dict = yaml.safe_load(f)
        
        # Load environment-specific config
        env_config_path = f'config/{env}/config.yml'
        if os.path.exists(env_config_path):
            with open(env_config_path, 'r') as f:
                env_config = yaml.safe_load(f)
                # Deep merge configurations
                config_dict = cls._deep_merge(config_dict, env_config)
        
        return cls(**config_dict)
    
    @staticmethod
    def _deep_merge(base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
        """Deep merge two dictionaries."""
        merged = base.copy()
        
        for key, value in override.items():
            if (
                key in merged 
                and isinstance(merged[key], dict) 
                and isinstance(value, dict)
            ):
                merged[key] = Config._deep_merge(merged[key], value)
            else:
                merged[key] = value
        
        return merged