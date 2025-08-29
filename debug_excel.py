import pandas as pd
import numpy as np

print("詳細檢查Excel文件內容")
print("=" * 40)

# 讀取Excel文件
df = pd.read_excel('test_results.xlsx', sheet_name='測試資料')

print(f"總行數: {len(df)}")
print(f"總列數: {len(df.columns)}")
print()

print("所有欄位名稱:")
for i, col in enumerate(df.columns):
    print(f"  {i+1}. '{col}'")
print()

print("每個欄位的資料狀況:")
for col in df.columns:
    null_count = df[col].isnull().sum()
    non_null_count = df[col].notna().sum()
    print(f"  {col}: {non_null_count} 有資料, {null_count} 無資料")
print()

print("前3筆完整資料:")
print("-" * 50)
for i in range(min(3, len(df))):
    print(f"第 {i+1} 筆:")
    row = df.iloc[i]
    for col in df.columns:
        value = row[col]
        if pd.isna(value):
            print(f"  {col}: [空值]")
        elif str(value).strip() == "":
            print(f"  {col}: [空字串]")
        else:
            print(f"  {col}: '{value}'")
    print()

# 特別檢查關鍵欄位
key_fields = ['author', 'supervisor', 'title']
print("關鍵欄位詳細檢查:")
for field in key_fields:
    if field in df.columns:
        print(f"\n{field} 欄位:")
        print(f"  資料類型: {df[field].dtype}")
        print(f"  空值數量: {df[field].isnull().sum()}")
        print(f"  空字串數量: {(df[field].astype(str).str.strip() == '').sum()}")
        print(f"  前5個值: {list(df[field].head())}")
    else:
        print(f"\n{field} 欄位: 不存在！")

print()
print("可能的問題診斷:")
if len(df) == 0:
    print("  - Excel文件沒有資料")
elif df.isnull().all().all():
    print("  - 所有資料都是空值") 
elif any(col not in df.columns for col in key_fields):
    print("  - 缺少關鍵欄位")
else:
    empty_fields = []
    for field in key_fields:
        if field in df.columns:
            if df[field].isnull().all():
                empty_fields.append(field)
    if empty_fields:
        print(f"  - 這些欄位完全是空的: {empty_fields}")
    else:
        print("  - 資料看起來正常")