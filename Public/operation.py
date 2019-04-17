import json
from Public.operationExcel import *

class OperationData:

    def __init__(self):
        self.excel=OperationExcel()

    def getRequestsData(self,row):
        '''获取请求参数'''
        return json.dumps(self.excel.getData(row=row))