"""Declare configuration settings and return as class"""
import os


class Config():
    """Basic configuration that can be extended"""

    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))


class ProdConfig(Config):
    """Production configuration."""

    ENV = "prod"
    DEBUG = False


class DevConfig(Config):
    """Development configuration."""

    ENV = "dev"
    DEBUG = True


class TestConfig(Config):
    """Test configuration."""

    ENV = "test"
    TESTING = True
    DEBUG = True
