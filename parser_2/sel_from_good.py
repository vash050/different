import sqlite3
from openpyxl import Workbook

conn = sqlite3.connect("parser_goods.sqlite3")
cursor = conn.cursor()
sql = "SELECT * FROM goods"
cursor.execute(sql)
list_values = cursor.fetchall() # or use fetchone()
print(list_values)

wb = Workbook()
sheet = wb.active
row = 1
sheet['B'+str(row)] = 'country'
sheet['C'+str(row)] = 'brand'
sheet['D'+str(row)] = 'collection'
sheet['E'+str(row)] = 'article'
sheet['F'+str(row)] = 'price'
sheet['G'+str(row)] = 'view'
sheet['H'+str(row)] = 'fastness_to_light'
sheet['I'+str(row)] = 'resistance_to_friction'
sheet['J'+str(row)] = 'width'
sheet['K'+str(row)] = 'repeat_drawing'
sheet['L'+str(row)] = 'length'
sheet['M'+str(row)] = 'description'
sheet['N'+str(row)] = 'link_to_photo'

# Заполнить данными
for item in list_values:
    row += 1
    sheet['A'+str(row)] = item[0]
    sheet['B'+str(row)] = item[1]
    sheet['C'+str(row)] = item[2].strip()
    sheet['D'+str(row)] = item[3]
    sheet['E' + str(row)] = item[4]
    sheet['F' + str(row)] = item[5][0:-6]
    sheet['G' + str(row)] = item[6]
    sheet['H' + str(row)] = item[7]
    sheet['I' + str(row)] = item[8]
    sheet['J' + str(row)] = item[9]
    sheet['K' + str(row)] = item[10]
    sheet['L' + str(row)] = item[11]
    sheet['M' + str(row)] = item[12].strip()
    sheet['N' + str(row)] = item[13]

wb.save('goods.xlsx')