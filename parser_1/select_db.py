import sqlite3
from openpyxl import Workbook

conn = sqlite3.connect("name_birds.sqlite3")
cursor = conn.cursor()
sql = "SELECT * FROM names"
cursor.execute(sql)
list_values = cursor.fetchall()  # or use fetchone()

wb = Workbook()
sheet = wb.active
row = 1
sheet['A'+str(row)] = 'Number'
sheet['B'+str(row)] = 'Russian'
sheet['C'+str(row)] = 'lat'
sheet['D'+str(row)] = 'Eng'

# Заполнить данными
for item in list_values:
    row += 1
    sheet['A'+str(row)] = item[0]
    sheet['B'+str(row)] = item[1]
    sheet['C'+str(row)] = item[2]
    sheet['D'+str(row)] = item[3]

wb.save('name_bird.xlsx')




# with open('name_bird.csv', 'w', encoding='utf-8') as f_obj:
#     for el in cursor.fetchall():
#         f_obj.write(f"{','.join(el[1:])}\n")
