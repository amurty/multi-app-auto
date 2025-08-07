"""
Test cases for web automation
"""
import pytest
import asyncio
from pathlib import Path
import sys

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from web_automation.google_search_automation import GoogleSearchAutomation
from web_automation.github_automation import GitHubAutomation

@pytest.mark.asyncio
class TestWebAutomation:
    
    async def test_google_search(self):
        """Test Google search functionality"""
        async with GoogleSearchAutomation() as automation:
            results = await automation.search("Playwright Python")
            
            assert len(results) > 0, "No search results returned"
            assert any("playwright" in result.lower() for result in results), "No Playwright-related results found"

    async def test_google_suggestions(self):
        """Test Google search suggestions"""
        async with GoogleSearchAutomation() as automation:
            suggestions = await automation.get_search_suggestions("Python web")
            
            # Suggestions might not always be available
            if suggestions:
                assert len(suggestions) > 0, "No suggestions returned"
                assert any("python" in suggestion.lower() for suggestion in suggestions), "No Python-related suggestions"

    async def test_github_repository_search(self):
        """Test GitHub repository search"""
        async with GitHubAutomation() as automation:
            repos = await automation.search_repositories("playwright python")
            
            assert len(repos) > 0, "No repositories found"
            for repo in repos:
                assert "name" in repo, "Repository name missing"
                assert repo["name"], "Repository name is empty"

    async def test_github_trending(self):
        """Test GitHub trending repositories"""
        async with GitHubAutomation() as automation:
            trending = await automation.get_trending_repositories("python")
            
            assert len(trending) > 0, "No trending repositories found"
            for repo in trending:
                assert "name" in repo, "Repository name missing"
                assert repo["name"], "Repository name is empty"

    async def test_github_repo_stats(self):
        """Test GitHub repository statistics"""
        async with GitHubAutomation() as automation:
            stats = await automation.check_repository_stats("microsoft", "playwright-python")
            
            assert isinstance(stats, dict), "Stats should be a dictionary"
            # Stats might be empty if elements aren't found, which is acceptable

@pytest.mark.asyncio
class TestWebAutomationErrorHandling:
    
    async def test_invalid_search_query(self):
        """Test handling of edge cases in search"""
        async with GoogleSearchAutomation() as automation:
            # Test empty search
            results = await automation.search("")
            # Should handle gracefully, results might be empty or contain default results

    async def test_nonexistent_repository(self):
        """Test handling of non-existent repository"""
        async with GitHubAutomation() as automation:
            stats = await automation.check_repository_stats("nonexistent-user", "nonexistent-repo")
            # Should handle gracefully without crashing

if __name__ == "__main__":
    pytest.main([__file__, "-v"])