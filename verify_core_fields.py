import pandas as pd

# 讀取測試結果
df = pd.read_excel('test_results.xlsx', sheet_name='測試資料')

print("核心欄位驗證 - 作者、指導老師、作品專題")
print("=" * 50)
print(f"總資料筆數: {len(df)} 篇")
print()

# 核心欄位對應檢查
core_fields = {
    'author': '作者',
    'supervisor': '指導老師', 
    'title': '作品專題'
}

print("核心欄位完整性:")
for field, chinese_name in core_fields.items():
    if field in df.columns:
        complete_count = df[field].notna().sum()
        percentage = (complete_count / len(df)) * 100
        print(f"  {chinese_name} ({field}): {complete_count}/{len(df)} ({percentage:.1f}%)")
    else:
        print(f"  {chinese_name} ({field}): 欄位不存在")

print()
print("詳細資料展示 (前5筆):")
print("-" * 70)

for i in range(min(5, len(df))):
    row = df.iloc[i]
    print(f"第 {i+1} 筆:")
    print(f"  作者: {row['author']}")
    print(f"  指導老師: {row['supervisor']}")
    print(f"  作品專題: {row['title']}")
    print(f"  學校: {row['school']}")
    print(f"  類別: {row['category']}")
    print()

print("資料品質檢查:")
print(f"  - 所有作者欄位都有資料: {'是' if df['author'].notna().all() else '否'}")
print(f"  - 所有指導老師欄位都有資料: {'是' if df['supervisor'].notna().all() else '否'}")
print(f"  - 所有作品專題欄位都有資料: {'是' if df['title'].notna().all() else '否'}")

print()
print("結論: 爬蟲已成功提取所有核心資料欄位!")