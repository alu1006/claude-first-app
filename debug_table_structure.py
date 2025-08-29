"""
Debug table structure to understand the correct column mapping
"""

import asyncio
from playwright.async_api import async_playwright
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class TableDebugger:
    def __init__(self):
        self.base_url = "https://www.shs.edu.tw/Customer/Winning/EssayIndex"
        
    async def debug_table_structure(self):
        """Debug the actual table structure"""
        
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            page = await browser.new_page()
            
            await page.goto(self.base_url)
            await page.wait_for_load_state('networkidle')
            await page.wait_for_timeout(3000)
            
            # Set search parameters
            logger.info("Setting search parameters...")
            await page.select_option('#contest-no', '1140315')
            await page.wait_for_timeout(500)
            
            await page.select_option('#cate-id', '13')  # 資訊類
            await page.wait_for_timeout(500)
            
            await page.select_option('#ranking', '1')  # 特優
            await page.wait_for_timeout(500)
            
            # Submit search
            logger.info("Submitting search...")
            search_btn = await page.wait_for_selector('#btnSearch', timeout=10000)
            await search_btn.click()
            await page.wait_for_load_state('networkidle')
            await page.wait_for_timeout(3000)
            
            # Debug table structure
            table_info = await page.evaluate('''
                () => {
                    const results = {
                        headers: [],
                        firstRowData: [],
                        tableHTML: ''
                    };
                    
                    // Get table headers
                    const headers = document.querySelectorAll('table thead tr th');
                    results.headers = Array.from(headers).map((th, index) => ({
                        index: index,
                        text: th.textContent?.trim() || '',
                        innerHTML: th.innerHTML
                    }));
                    
                    // Get first data row
                    const firstRow = document.querySelector('table tbody tr');
                    if (firstRow) {
                        const cells = firstRow.querySelectorAll('td');
                        results.firstRowData = Array.from(cells).map((td, index) => ({
                            index: index,
                            text: td.textContent?.trim() || '',
                            innerHTML: td.innerHTML
                        }));
                    }
                    
                    // Get table HTML for analysis
                    const table = document.querySelector('table');
                    if (table) {
                        results.tableHTML = table.outerHTML.substring(0, 2000); // First 2000 chars
                    }
                    
                    return results;
                }
            ''')
            
            print("=" * 60)
            print("表格結構分析")
            print("=" * 60)
            
            print("\n表格標題行:")
            for header in table_info['headers']:
                print(f"  欄位 {header['index']}: '{header['text']}'")
            
            print("\n第一筆資料:")
            for cell in table_info['firstRowData']:
                print(f"  欄位 {cell['index']}: '{cell['text']}'")
            
            print("\n表格HTML結構 (前2000字元):")
            print(table_info['tableHTML'])
            
            await page.wait_for_timeout(10000)  # Keep browser open for inspection
            await browser.close()

async def main():
    debugger = TableDebugger()
    await debugger.debug_table_structure()

if __name__ == "__main__":
    asyncio.run(main())