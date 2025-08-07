# Multi-App Automation with Playwright Python

A comprehensive automation framework for both web applications and desktop applications using Playwright Python.

## Features

- **Web Application Automation**: Automate web browsers and web applications
- **Desktop Application Automation**: Automate desktop applications including Electron apps
- **Cross-Platform Support**: Works on Windows, macOS, and Linux
- **Comprehensive Examples**: Ready-to-use examples for common automation tasks
- **Test Framework**: Built-in test cases using pytest
- **Flexible Configuration**: Easy-to-modify configuration settings

## Project Structure

```
multi-app-auto/
├── config/
│   └── config.py                 # Configuration settings
├── web_automation/
│   ├── base_web_automation.py    # Base class for web automation
│   ├── google_search_automation.py
│   └── github_automation.py
├── desktop_automation/
│   ├── base_desktop_automation.py # Base class for desktop automation
│   ├── calculator_automation.py
│   └── electron_app_automation.py
├── tests/
│   ├── test_web_automation.py
│   └── test_desktop_automation.py
├── examples/
│   └── workflow_example.py       # Complete workflow examples
├── requirements.txt
└── setup.py                     # Setup script
```

## Installation

1. **Clone the repository:**
```bash
git clone <your-repo-url>
cd multi-app-auto
```

2. **Run the setup script:**
```bash
python setup.py
```

This will:
- Install Python requirements
- Install Playwright browsers
- Create necessary directories

3. **Manual installation (alternative):**
```bash
pip install -r requirements.txt
playwright install
```

## Quick Start

### Web Automation Example

```python
import asyncio
from web_automation.google_search_automation import GoogleSearchAutomation

async def main():
    async with GoogleSearchAutomation() as automation:
        results = await automation.search("Playwright Python automation")
        for result in results:
            print(result)

asyncio.run(main())
```

### Desktop Automation Example

```python
import asyncio
from desktop_automation.calculator_automation import CalculatorAutomation

async def main():
    async with CalculatorAutomation() as calc:
        await calc.launch_and_setup()
        await calc.perform_calculation("25 + 17")

asyncio.run(main())
```

### Complete Workflow Example

```bash
python examples/workflow_example.py
```

## Configuration

Edit `config/config.py` to customize:

- Browser settings (headless mode, viewport size, timeout)
- Web URLs for automation
- Desktop application paths
- Screenshot settings
- Test configuration

## Web Automation Capabilities

### Google Search Automation
- Perform searches
- Get search suggestions
- Take screenshots of results

### GitHub Automation  
- Search repositories
- Get trending repositories
- Check repository statistics
- Automate navigation

### Base Web Features
- Navigate to URLs
- Click elements
- Fill forms
- Wait for elements
- Take screenshots
- Handle multiple browser types (Chromium, Firefox, WebKit)

## Desktop Automation Capabilities

### Calculator Automation
- Launch calculator application
- Perform calculations
- Clear calculator
- Cross-platform support

### Electron App Automation
- Connect to Electron apps via Chrome DevTools Protocol
- Automate menu actions
- Fill forms
- Test keyboard shortcuts
- Support for VS Code and other Electron apps

### Base Desktop Features
- Launch desktop applications
- Take screenshots
- Handle keyboard input
- Connect to debugging ports
- Cross-platform application paths

## Running Tests

Run all tests:
```bash
pytest tests/ -v
```

Run specific test files:
```bash
pytest tests/test_web_automation.py -v
pytest tests/test_desktop_automation.py -v
```

Run with HTML report:
```bash
pytest tests/ --html=reports/report.html
```

## Platform-Specific Notes

### macOS
- Calculator app path: `/System/Applications/Calculator.app`
- Use `open` command to launch apps
- Some apps may require accessibility permissions

### Windows  
- Calculator app: `calc.exe`
- Direct executable launching
- May require running as administrator for some apps

### Linux
- Calculator app: `gnome-calculator` (or equivalent)
- Package manager installation may be required
- X11 or Wayland display server considerations

## Advanced Usage

### Custom Desktop App Automation

```python
from desktop_automation.base_desktop_automation import BaseDesktopAutomation

class MyAppAutomation(BaseDesktopAutomation):
    def __init__(self):
        super().__init__("/path/to/my/app")
    
    async def my_custom_automation(self):
        await self.setup()
        # Your automation logic here
        await self.teardown()
```

### Custom Web Automation

```python
from web_automation.base_web_automation import BaseWebAutomation

class MyWebAutomation(BaseWebAutomation):
    async def automate_my_site(self):
        await self.navigate_to("https://mysite.com")
        # Your automation logic here
```

## Troubleshooting

### Common Issues

1. **Browser not found**: Run `playwright install` to install browsers
2. **Desktop app not launching**: Check app paths in `config/config.py`
3. **Permission errors**: On macOS, grant accessibility permissions
4. **Timeouts**: Adjust timeout values in configuration

### Dependencies

For desktop automation with keystroke simulation:
```bash
pip install pyautogui  # Optional, for keystroke simulation
```

### Debugging

Enable debug logging:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## License

This project is open source. Please check the license file for details.

## Support

For issues and questions:
- Check the troubleshooting section
- Review the examples
- Check existing issues
- Create a new issue with detailed information