"""
Test cases for desktop automation
"""
import pytest
import asyncio
import platform
from pathlib import Path
import sys

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from desktop_automation.calculator_automation import CalculatorAutomation
from desktop_automation.base_desktop_automation import BaseDesktopAutomation

@pytest.mark.asyncio
class TestDesktopAutomation:
    
    @pytest.mark.skipif(platform.system() not in ["Windows", "Darwin", "Linux"], 
                       reason="Unsupported platform")
    async def test_calculator_launch(self):
        """Test calculator application launch"""
        async with CalculatorAutomation() as calc:
            # Test setup
            await calc.setup()
            assert calc.playwright is not None, "Playwright not initialized"
            assert calc.browser is not None, "Browser not initialized"

    async def test_base_desktop_automation_setup(self):
        """Test base desktop automation setup"""
        automation = BaseDesktopAutomation()
        
        await automation.setup()
        
        assert automation.playwright is not None, "Playwright not initialized"
        assert automation.browser is not None, "Browser not initialized"
        assert automation.context is not None, "Context not initialized"
        assert automation.page is not None, "Page not initialized"
        
        await automation.teardown()

    async def test_screenshot_capability(self):
        """Test screenshot functionality"""
        automation = BaseDesktopAutomation()
        
        await automation.setup()
        
        # Take a screenshot
        screenshot_path = await automation.take_screenshot("test_screenshot")
        
        assert screenshot_path.exists(), "Screenshot file was not created"
        assert screenshot_path.suffix == ".png", "Screenshot is not a PNG file"
        
        # Cleanup
        if screenshot_path.exists():
            screenshot_path.unlink()
        
        await automation.teardown()

@pytest.mark.asyncio 
class TestCalculatorAutomation:
    
    @pytest.mark.skipif(platform.system() not in ["Windows", "Darwin", "Linux"],
                       reason="Calculator not available on this platform")
    async def test_calculator_initialization(self):
        """Test calculator automation initialization"""
        calc = CalculatorAutomation()
        
        # Check if app path is set correctly for the current platform
        system = platform.system().lower()
        expected_paths = {
            "windows": "calc.exe",
            "darwin": "/System/Applications/Calculator.app",
            "linux": "gnome-calculator"
        }
        
        if system in expected_paths:
            assert calc.app_path == expected_paths[system], f"Incorrect app path for {system}"

    @pytest.mark.skipif(platform.system() not in ["Darwin"], 
                       reason="macOS Calculator specific test")
    async def test_macos_calculator_path(self):
        """Test macOS calculator path"""
        calc = CalculatorAutomation()
        expected_path = "/System/Applications/Calculator.app"
        assert calc.app_path == expected_path, "Incorrect macOS Calculator path"

@pytest.mark.asyncio
class TestDesktopAutomationErrorHandling:
    
    async def test_invalid_app_path(self):
        """Test handling of invalid application path"""
        automation = BaseDesktopAutomation("/invalid/path/to/app")
        
        # Should not raise exception during initialization
        await automation.setup()
        
        # But should handle gracefully when trying to launch
        try:
            automation.launch_desktop_app()
        except Exception as e:
            assert "Failed to launch app" in str(e)
        
        await automation.teardown()

    async def test_connection_timeout(self):
        """Test connection timeout handling"""
        automation = BaseDesktopAutomation()
        await automation.setup()
        
        # Test connection to non-existent debug port
        result = await automation.connect_to_electron_app(99999)
        assert result is False, "Should return False for invalid connection"
        
        await automation.teardown()

if __name__ == "__main__":
    pytest.main([__file__, "-v"])