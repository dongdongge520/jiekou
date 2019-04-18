import xlrd
from Public.getcwd import data_dir
from Public.excel_data import *

class OperationExcel:

    def getExcel(self):
        '''打开Excel'''
        db = xlrd.open_workbook(data_dir('data','data.xlsx'))
        sheet = db.sheet_by_index(0)
        return sheet

    def get_rows(self):
        '''获取Excel的行数'''
        return self.getExcel().nrows

    def get_row_col(self,row,col):
        '''获取单元格内容'''
        return self.getExcel().cell_value(row,col)

    def getUrl(self,row):
        '''获取URL'''
        return self.get_row_col(row,getUrl())

    def getHeaders(self,row):
        '''获取headers'''
        return self.get_row_col(row,getHeaders())

    def getData(self,row):
        '''获取data'''
        return self.get_row_col(row,getData())

    def getExpect(self,row):
        '''获取Expect'''
        return self.get_row_col(row,getExpect())

    def getResult(self,row):
        '''获取Result'''
        return self.get_row_col(row,getResult())

# operation = OperationExcel()
# print(operation.getHeaders(1),type(operation.getHeaders(1)))

