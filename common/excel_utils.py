"""
@备注：xlrd读取文件，合并单元格，读取数据排序
@作者：张文
@日期：2020.07.04
"""
import xlrd
import os
from common.setting_path import *
from xlutils.copy import copy
import inspect
excel_path = os.path.join(os.path.dirname(os.path.dirname(__file__)) , 'data/test_data.xlsx' )
print( excel_path )
class readExcelXlrd:
    """用xlrd操作excel的类"""
    def __init__(self,file_path,sheet_name):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.sheet = self.get_sheet()
        self.wb = xlrd.open_workbook(self.file_path,formatting_info=True)

    # def read_excel_column(self, col):
    #     """
    #     返回第col列的数据
    #     :param col：int类型  具体需要返回数据的列数，
    #     :return col_data: lits类型  返回col列的全部数据
    #     """
    #     wb = xlrd.open_workbook(excel_path)
    #     sheet_name = wb.sheet_by_name("Sheet1")
    #     col_data = sheet_name.col_values(col)  # 返回由该列中所有单元格的数据组成的列表
    #     return col_data
    #
    #
    # def get_sheet(self):
    #     """返回sheet"""
    #     wb = xlrd.open_workbook(self.file_path)
    #     sheet = wb.sheet_by_name(self.sheet_name)
    #     return sheet
    #
    # def get_row_count(self):
    #     """返回excel行数"""
    #     row_count = self.sheet.nrows
    #     return row_count
    #
    # def get_col_count(self):
    #     """返回excel列数"""
    #     col_count = self.sheet.ncols
    #     return col_count

    # def get_merged_cell_value(self, row_index, col_index):
    #     """
    #     根据输入坐标，输出合并单元格或者普通单元格的值
    #     :param row_index int型，行数
    #     :param col_index int型，列数
    #     :return ：返回对应坐标的值
    #     """
    #     workbook = xlrd.open_workbook(self.file_path)
    #     sheet = workbook.sheet_by_name(self.sheet_name)
    #     # merged_cells 获取当前表格所有合并单元格的位置信息 ，返回一个列
    #     merged = sheet.merged_cells
    #     cell_value = None
    #     for (rlow, rhigh, clow, chigh) in merged:  # 遍历表格中所有合并单元格位置信息
    #         if (row_index >= rlow and row_index < rhigh):  # 行坐标判断
    #             if (col_index >= clow and col_index < chigh):  # 列坐标判断
    #                 # 如果满足条件，就把合并单元格第一个位置的值赋给其它合并单元格
    #                 cell_value = sheet.cell_value(rlow, clow)
    #                 break
    #             else:
    #                 cell_value =sheet.cell_value(row_index,col_index) #如果不是合并单元格，直接输出普通单元格的值
    #                 return cell_value
    #         else:
    #             cell_value = sheet.cell_value(row_index, col_index)  # 如果不是合并单元格，直接输出普通单元格的值
    #     return cell_value
    def get_sheet(self):
        wb = xlrd.open_workbook(self.file_path)
        sheet = wb.sheet_by_name(self.sheet_name)
        return sheet

    def get_row_count(self):
        row_count = self.sheet.nrows
        return row_count

    def get_col_count(self):
        col_count = self.sheet.ncols
        return col_count

    def __get_cell_value(self,row_index, col_index):
        cell_value = self.sheet.cell_value(row_index,col_index)
        return cell_value

    def get_merged_info(self):
        merged_info = self.sheet.merged_cells
        return merged_info
    def get_merged_cell_value(self,row_index, col_index):
        """既能获取普通单元格的数据又能获取合并单元格数据"""
        cell_value = None
        for (rlow, rhigh, clow, chigh) in self.get_merged_info():
            if (row_index >= rlow and row_index < rhigh):
                if (col_index >= clow and col_index < chigh):
                    cell_value = self.__get_cell_value(rlow, clow)
                    break # 防止循环去进行判断出现值覆盖的情况
                else:
                    cell_value = self.__get_cell_value(row_index, col_index)
            else:
                cell_value = self.__get_cell_value(row_index, col_index)
        return cell_value

    def get_sheet_by_dict(self):
        """把获取的sheet数据转化为字典"""
        all_data_list = []
        first_row = self.sheet.row(0)
        for row in range(1, self.get_row_count()):
            row_dict = {}
            for col in range(0, self.get_col_count()):
                row_dict[first_row[col].value] = self.get_merged_cell_value(row, col)
            all_data_list.append(row_dict)
        return all_data_list

    def update_excel_data(self, row_id, col_id, content):
        """更新excel对应坐标的数据"""
        new_wb = copy(self.wb)
        sheet = new_wb.get_sheet(self.wb.sheet_names().index(self.sheet_name))
        sheet.write(row_id, col_id, content)
        new_wb.save(self.file_path)

    def clear_excel_cloumn(self, start_id, end_id, col_id):
        """清空某一行的数据"""
        new_wb = copy(self.wb)
        sheet = new_wb.get_sheet(self.wb.sheet_names().index(self.sheet_name))
        for row in range(start_id, end_id):
            sheet.write(row, col_id, '')
        new_wb.save(self.file_path)

if __name__ == "__main__":
    excel_path = os.path.join(data_path, 'test_case.xlsx')
    print(excel_path)
    excel = readExcelXlrd(excel_path, 'Sheet1')
    #print(excel.read_excel_column(2)) #作业第一题，返回第二列的全部数据
    # print(excel.excel_merge_cell(4,0)) #作业第二题，合并单元格情况
    # print(excel.excel_merge_cell(2, 2))#作业第二题，普通单元格情况
    # list_grade = excel.read_excel_column(3)[1:] #作业第三题，去掉第一行的中文
    # list_grade.sort(reverse=True)  #通过列表的sort方法中参数reverse，让数据倒序排序
    # print(list_grade) #打印排序后的列表
    # 第四题写博客 https: // www.cnblogs.com / ceshixiaowen / p / 13234922.html
    for i in excel.get_sheet_by_dict():
        print(i)


