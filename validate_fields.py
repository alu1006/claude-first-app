import pandas as pd

print("欄位規格驗證 - 對照CLAUDE.md規格")
print("=" * 50)

# 讀取測試結果
df = pd.read_excel('test_results.xlsx', sheet_name='測試資料')

# 定義預期欄位
main_fields = {
    'author': '作者 - 學生姓名',
    'supervisor': '指導老師 - 指導教師姓名',
    'title': '作品專題 - 小論文標題'
}

auxiliary_fields = {
    'school': '學校 - 學校名稱',
    'category': '類別 - 競賽類別',
    'competition_period': '期數 - 競賽期數',
    'ranking': '等級 - 獲獎等級',
    'pdf_link': 'PDF鏈接 - 完整的PDF下載連結'
}

print("🎯 主要欄位驗證:")
for field, description in main_fields.items():
    if field in df.columns:
        complete_count = df[field].notna().sum()
        status = "✅" if complete_count == len(df) else "❌"
        print(f"  {status} {description}: {complete_count}/{len(df)}")
    else:
        print(f"  ❌ {description}: 欄位不存在")

print()
print("📊 輔助欄位驗證:")
for field, description in auxiliary_fields.items():
    if field in df.columns:
        complete_count = df[field].notna().sum()
        status = "✅" if complete_count == len(df) else "❌"
        print(f"  {status} {description}: {complete_count}/{len(df)}")
    else:
        print(f"  ❌ {description}: 欄位不存在")

print()
print("詳細資料展示 (驗證規格符合性):")
print("-" * 60)
sample_row = df.iloc[0]
print(f"樣本資料:")
print(f"  🎯 作者: '{sample_row['author']}'")
print(f"  🎯 指導老師: '{sample_row['supervisor']}'")
print(f"  🎯 作品專題: '{sample_row['title']}'")
print(f"  📊 學校: '{sample_row['school']}'")
print(f"  📊 類別: '{sample_row['category']}'")
print(f"  📊 期數: '{sample_row['competition_period']}'")
print(f"  📊 等級: '{sample_row['ranking']}'")
print(f"  📊 PDF鏈接: '{sample_row['pdf_link']}'")

print()
print("結論:")
all_main_complete = all(df[field].notna().all() for field in main_fields.keys() if field in df.columns)
all_aux_complete = all(df[field].notna().all() for field in auxiliary_fields.keys() if field in df.columns)

if all_main_complete and all_aux_complete:
    print("✅ 完全符合CLAUDE.md規格要求！")
    print("✅ 所有主要欄位和輔助欄位都完整提取")
else:
    print("❌ 部分欄位不符合規格要求")