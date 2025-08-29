import pandas as pd

df = pd.read_excel('test_results.xlsx', sheet_name='測試資料')

print("執行結果確認:")
print(f"總論文數: {len(df)}")
print()

print("所有欄位:")
for col in df.columns:
    print(f"  {col}")
print()

print("必要資料檢查:")
print(f"學生姓名 (author): {df['author'].notna().sum()}/{len(df)}")
print(f"指導老師 (supervisor): {df['supervisor'].notna().sum()}/{len(df)}")  
print(f"論文標題 (title): {df['title'].notna().sum()}/{len(df)}")
print(f"PDF鏈接 (pdf_link): {df['pdf_link'].notna().sum()}/{len(df)}")
print()

print("資料樣本:")
for i in range(3):
    row = df.iloc[i]
    print(f"第{i+1}篇:")
    print(f"  學生: {row['author']}")
    print(f"  老師: {row['supervisor']}")
    print(f"  標題: {row['title']}")
    print(f"  PDF: {row['pdf_link']}")
    print()