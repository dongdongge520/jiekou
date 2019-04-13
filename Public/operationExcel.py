import xlrd
from Public.getcwd import data_dir

class OperationExcel:

    def getExcel(self):
        db = xlrd.open_workbook(data_dir('data','data.xlsx'))
        sheet = db.sheet_by_index(0)
        return sheet

operation = OperationExcel()
print(operation.getExcel())