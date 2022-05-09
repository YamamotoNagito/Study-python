import openpyxl

# エクセルファイルの読み込み
# wb = openpyxl.load_workbook("Sample.xlsx")

# エクセルファイルの新規作成
wb = openpyxl.Workbook()

# エクセルファイルの保存
# 上書き保存（読み込んだのと同じ名前を指定）
wb.save("./excel/Sample2.xlsx")

# 別名保存（読み込んだのと別名を指定）
# wb.save("Sample2.xlsx")