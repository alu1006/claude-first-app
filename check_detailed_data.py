import pandas as pd

# 讀取測試結果
df = pd.read_excel('test_results.xlsx', sheet_name='測試資料')

print("=== 詳細資料檢查 ===")
print(f"總論文數: {len(df)}")
print()

# 檢查所有欄位
print("可用欄位:")
for col in df.columns:
    print(f"  {col}")
print()

# 檢查學生名字、指導老師、小論文名稱
required_fields = ['author', 'supervisor', 'title']
print("必要欄位檢查:")
for field in required_fields:
    if field in df.columns:
        non_null_count = df[field].notna().sum()
        print(f"  {field}: {non_null_count} / {len(df)} 篇有資料")
    else:
        print(f"  {field}: 欄位不存在")
print()

# 顯示完整資料樣本
print("前5筆完整資料:")
if len(df) > 0:
    sample_cols = ['school', 'author', 'supervisor', 'title', 'pdf_link']
    available_cols = [col for col in sample_cols if col in df.columns]
    print(df[available_cols].head().to_string())
else:
    print("無資料")