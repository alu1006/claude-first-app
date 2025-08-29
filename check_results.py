import pandas as pd

# 讀取測試結果
df = pd.read_excel('test_results.xlsx', sheet_name='測試資料')

print("=== 測試結果檢查 ===")
print(f"總論文數: {len(df)}")
print()

# 類別統計
print("類別統計:")
for category, count in df['category'].value_counts().items():
    print(f"  {category}: {count} 篇")
print()

# 檢查PDF鏈接
pdf_links_count = df['pdf_link'].notna().sum()
print(f"有PDF鏈接的論文: {pdf_links_count} / {len(df)}")
print()

# 顯示前幾個PDF鏈接樣本
print("PDF鏈接樣本:")
for i, row in df.head(3).iterrows():
    print(f"{i+1}. {row['title']}")
    print(f"   PDF: {row['pdf_link']}")
    print()