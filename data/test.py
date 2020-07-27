import xlrd
my_excel = xlrd.open_workbook("./test.xlsx") #读取excel文件，相当于打开excel
my_sheet = my_excel.sheet_by_name("Sheet1") #通过sheet页的名字，跳转sheet页
#获取数据的最大行数
max_row = my_sheet.nrows
#获取最大列数
max_col = my_sheet.ncols
#获取某一列的数据,
my_sheet.col_values(2) #返回第二列的列表
#获取某一行的数据
my_sheet.row_values(2) #返回第二列的列表
#获取某个坐标的值
a = my_sheet.cell_value(2,0)

a = my_sheet.merged_cells

row_index = 3  #输入合并单元格行数
col_index = 0  #输入合并单元格列数
merged = my_sheet.merged_cells
print(merged)
for(rlow, rhigh, clow, chigh) in merged:  # 遍历表格中所有合并单元格位置信息
    if (row_index >= rlow and row_index < rhigh):  # 行坐标判断,判断输入的值  1=< row_index <4
        if (col_index >= clow and col_index < chigh):  # 列坐标判断    0 =<col_index < 1
            # 如果满足条件，就把合并单元格第一个位置的值赋给其它合并单元格
            cell_value = my_sheet.cell_value(rlow, clow)
print(cell_value)