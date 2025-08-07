"""
Configuration settings for automation
"""
import os
from pathlib import Path

# Base paths
BASE_DIR = Path(__file__).parent.parent
REPORTS_DIR = BASE_DIR / "reports"
SCREENSHOTS_DIR = BASE_DIR / "screenshots"

# Browser settings
DEFAULT_BROWSER = "chromium"  # chromium, firefox, webkit
HEADLESS = False
VIEWPORT = {"width": 1920, "height": 1080}
TIMEOUT = 30000  # 30 seconds

# Web automation settings
WEB_URLS = {
    "google": "https://www.google.com",
    "github": "https://github.com",
    "example": "https://example.com"
}

# Desktop automation settings
DESKTOP_APPS = {
    "calculator": {
        "windows": "calc.exe",
        "macos": "/System/Applications/Calculator.app",
        "linux": "gnome-calculator"
    },
    "notepad": {
        "windows": "notepad.exe",
        "macos": "/System/Applications/TextEdit.app",
        "linux": "gedit"
    }
}

# Test settings
PARALLEL_WORKERS = 4
RETRY_COUNT = 2
SLOW_MO = 100  # milliseconds

# Screenshot settings
SCREENSHOT_ON_FAILURE = True
FULL_PAGE_SCREENSHOTS = True