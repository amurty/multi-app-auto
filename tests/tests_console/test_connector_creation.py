"""
Test cases for connector creation functionality
"""
import pytest
import asyncio
from pathlib import Path
import sys
from playwright.async_api import async_playwright

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from qa_lib.config import *

@pytest.mark.asyncio
class TestConnectorCreation:
    
    async def test_login_and_navigate(self):
        """Test login to BNN console and navigate to connector creation"""
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            page = await browser.new_page()
            
            try:
                # Navigate to the URL
                await page.goto("https://release.bnntest.com/")
                
                # Enter organization name
                await page.fill('input[name="orgName"]', "qa-rel-global-ent")
                await page.click('button[type="submit"]')
                
                # Wait for login page and enter credentials
                await page.wait_for_selector('input[type="email"]')
                await page.fill('input[type="email"]', "ashwini.murty@banyansecurity.io")
                await page.fill('input[type="password"]', "Test123!")
                await page.click('button[type="submit"]')
                
                # Wait for dashboard to load
                await page.wait_for_load_state('networkidle')
                
                # Take screenshot for verification
                await page.screenshot(path="login_success.png")
                
                # Verify successful login by checking for dashboard elements
                dashboard_element = await page.wait_for_selector('[data-testid="dashboard"]', timeout=10000)
                assert dashboard_element is not None, "Dashboard not loaded after login"
                
            finally:
                await browser.close()
    
    async def test_create_basic_connector(self):
        """Test creation of a basic connector"""
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            page = await browser.new_page()
            
            try:
                # Login first
                await self._login_to_console(page)
                
                # Navigate to connector creation
                await page.click('text="Connectors"')
                await page.click('text="Create Connector"')
                
                # Fill connector details (adjust selectors based on actual UI)
                await page.fill('input[name="connectorName"]', "Test Connector")
                await page.select_option('select[name="connectorType"]', "Basic")
                
                # Submit connector creation
                await page.click('button[type="submit"]')
                
                # Verify connector was created
                await page.wait_for_selector('text="Connector created successfully"')
                
            finally:
                await browser.close()
    
    async def test_connector_with_credentials(self):
        """Test connector creation with authentication credentials"""
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            page = await browser.new_page()
            
            try:
                # Login and navigate to connector creation
                await self._login_to_console(page)
                await self._navigate_to_connector_creation(page)
                
                # Fill connector with credentials
                await page.fill('input[name="connectorName"]', "Authenticated Connector")
                await page.fill('input[name="username"]', "testuser")
                await page.fill('input[name="password"]', "testpass")
                
                # Submit and verify
                await page.click('button[type="submit"]')
                await page.wait_for_selector('text="Connector created successfully"')
                
            finally:
                await browser.close()
    
    async def test_connector_validation(self):
        """Test connector configuration validation"""
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            page = await browser.new_page()
            
            try:
                # Login and navigate to connector creation
                await self._login_to_console(page)
                await self._navigate_to_connector_creation(page)
                
                # Try to submit without required fields
                await page.click('button[type="submit"]')
                
                # Verify validation error appears
                validation_error = await page.wait_for_selector('text="Name is required"')
                assert validation_error is not None, "Validation error not shown"
                
            finally:
                await browser.close()
    
    async def test_connector_connection_test(self):
        """Test connector connection functionality"""
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            page = await browser.new_page()
            
            try:
                # Login and create a connector first
                await self._login_to_console(page)
                await self._create_test_connector(page)
                
                # Test the connection
                await page.click('button[data-testid="test-connection"]')
                await page.wait_for_selector('text="Connection successful"')
                
            finally:
                await browser.close()
    
    async def _login_to_console(self, page):
        """Helper method to login to the console"""
        await page.goto("https://release.bnntest.com/")
        await page.fill('input[name="orgName"]', "qa-rel-global-ent")
        await page.click('button[type="submit"]')
        await page.wait_for_selector('input[type="email"]')
        await page.fill('input[type="email"]', "ashwini.murty@banyansecurity.io")
        await page.fill('input[type="password"]', "Test123!")
        await page.click('button[type="submit"]')
        await page.wait_for_load_state('networkidle')
    
    async def _navigate_to_connector_creation(self, page):
        """Helper method to navigate to connector creation page"""
        await page.click('text="Connectors"')
        await page.click('text="Create Connector"')
    
    async def _create_test_connector(self, page):
        """Helper method to create a test connector"""
        await self._navigate_to_connector_creation(page)
        await page.fill('input[name="connectorName"]', "Test Connection Connector")
        await page.click('button[type="submit"]')
        await page.wait_for_selector('text="Connector created successfully"')

@pytest.mark.asyncio
class TestConnectorErrorHandling:
    
    async def test_invalid_connector_config(self):
        """Test handling of invalid connector configuration"""
        # This is a placeholder test - implement based on your connector requirements
        pass
    
    async def test_connection_timeout(self):
        """Test connection timeout handling"""
        # This is a placeholder test - implement based on your connector requirements
        pass
    
    async def test_authentication_failure(self):
        """Test authentication failure handling"""
        # This is a placeholder test - implement based on your connector requirements
        pass

if __name__ == "__main__":
    pytest.main([__file__, "-v"])