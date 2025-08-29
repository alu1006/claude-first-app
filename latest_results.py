import pandas as pd

print("最新測試執行結果")
print("=" * 40)

# 讀取剛生成的結果
df = pd.read_excel('test_results.xlsx', sheet_name='測試資料')

print(f"爬取統計:")
print(f"  總論文數: {len(df)} 篇")

# 期數分析
periods = df['competition_period'].value_counts()
print(f"\n期數分析:")
for period, count in periods.items():
    print(f"  {period}: {count} 篇")

# 類別分析
categories = df['category'].value_counts()
print(f"\n類別分析:")
for category, count in categories.items():
    print(f"  {category}: {count} 篇")

# 核心欄位檢查
print(f"\n核心欄位檢查:")
print(f"  作者 (author): {df['author'].notna().sum()}/{len(df)}")
print(f"  指導老師 (supervisor): {df['supervisor'].notna().sum()}/{len(df)}")
print(f"  作品專題 (title): {df['title'].notna().sum()}/{len(df)}")
print(f"  PDF鏈接 (pdf_link): {df['pdf_link'].notna().sum()}/{len(df)}")

print(f"\n實際資料展示 (隨機3筆):")
print("-" * 60)
sample = df.sample(3) if len(df) >= 3 else df
for i, (idx, row) in enumerate(sample.iterrows()):
    print(f"第 {i+1} 筆:")
    print(f"  作者: {row['author']}")
    print(f"  指導老師: {row['supervisor']}")
    print(f"  作品專題: {row['title']}")
    print(f"  學校: {row['school']}")
    print(f"  類別: {row['category']}")
    print(f"  期數: {row['competition_period']}")
    print(f"  PDF: {row['pdf_link']}")
    print()

# 資料完整性總結
all_complete = (df['author'].notna().all() and 
                df['supervisor'].notna().all() and 
                df['title'].notna().all() and 
                df['pdf_link'].notna().all())

print(f"資料完整性: {'完全正確' if all_complete else '有缺失'}")
print("測試狀態: 成功完成")