#!/usr/bin/env python3
"""
Setup script for Playwright automation environment
"""
import subprocess
import sys
import os

def install_requirements():
    """Install Python requirements"""
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)

def install_playwright_browsers():
    """Install Playwright browsers"""
    subprocess.run([sys.executable, "-m", "playwright", "install"], check=True)

def create_directories():
    """Create necessary directories"""
    directories = [
        "web_automation",
        "desktop_automation", 
        "tests",
        "reports",
        "screenshots",
        "config"
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Created directory: {directory}")

if __name__ == "__main__":
    print("Setting up Playwright automation environment...")
    
    print("1. Creating directories...")
    create_directories()
    
    print("2. Installing Python requirements...")
    install_requirements()
    
    print("3. Installing Playwright browsers...")
    install_playwright_browsers()
    
    print("Setup complete!")