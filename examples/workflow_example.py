"""
Example automation workflow combining web and desktop automation
"""
import asyncio
import sys
from pathlib import Path

# Add parent directories to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from web_automation.google_search_automation import GoogleSearchAutomation
from web_automation.github_automation import GitHubAutomation
from desktop_automation.calculator_automation import CalculatorAutomation

class AutomationWorkflow:
    """
    Combined automation workflow example
    """
    
    def __init__(self):
        self.results = {}

    async def research_workflow(self):
        """
        Research workflow: Search for information and gather data
        """
        print("=== Starting Research Workflow ===")
        
        # Step 1: Search Google for Python automation tools
        print("\n1. Searching Google for Python automation tools...")
        async with GoogleSearchAutomation() as google:
            search_results = await google.search("Python automation tools 2024")
            self.results['google_search'] = search_results
            
            print(f"Found {len(search_results)} search results:")
            for i, result in enumerate(search_results[:3], 1):
                print(f"   {i}. {result}")

        # Step 2: Find GitHub repositories
        print("\n2. Searching GitHub for automation repositories...")
        async with GitHubAutomation() as github:
            repo_results = await github.search_repositories("python automation framework")
            self.results['github_repos'] = repo_results
            
            print(f"Found {len(repo_results)} repositories:")
            for repo in repo_results[:3]:
                print(f"   - {repo['name']}: {repo['description'][:100]}...")

        # Step 3: Check trending automation tools
        print("\n3. Checking trending Python repositories...")
        async with GitHubAutomation() as github:
            trending = await github.get_trending_repositories("python")
            self.results['trending_repos'] = trending
            
            automation_trending = [repo for repo in trending if 
                                 'automation' in repo['name'].lower() or 
                                 'automation' in repo['description'].lower()]
            
            if automation_trending:
                print("Trending automation repositories:")
                for repo in automation_trending[:3]:
                    print(f"   - {repo['name']} ({repo['stars']} stars)")
            else:
                print("No automation-specific trending repositories found")

    async def productivity_workflow(self):
        """
        Productivity workflow: Automate daily tasks
        """
        print("\n=== Starting Productivity Workflow ===")
        
        # Step 1: Use calculator for some computations
        print("\n1. Performing calculations...")
        async with CalculatorAutomation() as calc:
            success = await calc.launch_and_setup()
            
            if success:
                calculations = [
                    "25 * 4",
                    "150 + 75", 
                    "1000 / 8"
                ]
                
                for calculation in calculations:
                    print(f"   Computing: {calculation}")
                    await calc.perform_calculation(calculation)
                    await calc.clear_calculator()
                    await asyncio.sleep(1)
                    
                self.results['calculations'] = calculations
            else:
                print("   Calculator automation not available on this system")

    async def data_collection_workflow(self):
        """
        Data collection workflow: Gather specific information
        """
        print("\n=== Starting Data Collection Workflow ===")
        
        # Collect data about popular Python tools
        tools_to_research = ["playwright", "selenium", "pyautogui"]
        
        async with GitHubAutomation() as github:
            for tool in tools_to_research:
                print(f"\n   Researching {tool}...")
                
                # Search for the main repository
                repos = await github.search_repositories(f"{tool} python")
                
                if repos:
                    main_repo = repos[0]  # Assume first result is the main repo
                    print(f"   Main repository: {main_repo['name']}")
                    print(f"   Description: {main_repo['description'][:100]}...")
                    
                    # Try to get detailed stats (this might not always work)
                    if '/' in main_repo['name']:
                        owner, repo_name = main_repo['name'].split('/')[:2]
                        stats = await github.check_repository_stats(owner, repo_name)
                        
                        if stats:
                            print(f"   Stats: {stats}")
                
                await asyncio.sleep(1)  # Be nice to GitHub

    async def run_complete_workflow(self):
        """
        Run the complete automation workflow
        """
        start_time = asyncio.get_event_loop().time()
        
        try:
            # Run research workflow
            await self.research_workflow()
            
            # Run productivity workflow  
            await self.productivity_workflow()
            
            # Run data collection workflow
            await self.data_collection_workflow()
            
        except Exception as e:
            print(f"Error in workflow: {e}")
        
        finally:
            end_time = asyncio.get_event_loop().time()
            duration = end_time - start_time
            
            print(f"\n=== Workflow Complete ===")
            print(f"Total execution time: {duration:.2f} seconds")
            print(f"Results collected: {len(self.results)} categories")
            
            # Summary
            self.print_summary()

    def print_summary(self):
        """Print workflow results summary"""
        print("\n=== Workflow Summary ===")
        
        for category, data in self.results.items():
            if isinstance(data, list):
                print(f"{category}: {len(data)} items")
            else:
                print(f"{category}: {data}")

class DemoWorkflow:
    """
    Simplified demo workflow for testing
    """
    
    async def quick_demo(self):
        """Quick demonstration of capabilities"""
        print("=== Quick Demo Workflow ===")
        
        # Quick web search
        print("\n1. Quick Google search...")
        async with GoogleSearchAutomation() as google:
            results = await google.search("Playwright automation")
            print(f"   Found {len(results)} results")
            if results:
                print(f"   Top result: {results[0]}")

        # Quick GitHub search
        print("\n2. Quick GitHub search...")
        async with GitHubAutomation() as github:
            repos = await github.search_repositories("playwright")
            print(f"   Found {len(repos)} repositories")
            if repos:
                print(f"   Top repo: {repos[0]['name']}")

        print("\nDemo completed!")

async def main():
    """Main execution function"""
    print("Multi-App Automation Workflow")
    print("=" * 40)
    
    choice = input("\nChoose workflow:\n1. Complete workflow\n2. Quick demo\nEnter choice (1 or 2): ").strip()
    
    if choice == "2":
        demo = DemoWorkflow()
        await demo.quick_demo()
    else:
        workflow = AutomationWorkflow()
        await workflow.run_complete_workflow()

if __name__ == "__main__":
    asyncio.run(main())