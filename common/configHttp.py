from Public.operationExcel import *
from Public.log import MyLog
import requests
import json


class ConfigHttp:
    def __init__(self):
        self.excel=OperationExcel()
        self.log=MyLog('weather')

    def get(self,row):
        '''重新封装get请求'''
        try:
            self.log.info('<----------------------开始get请求----------------------->')
            r = requests.get(
                url=self.excel.getUrl(row),
                headers=json.loads(self.excel.getHeaders(row)),
                data=self.excel.getData(row))
            status = r.status_code  #获取返回的协议状态码
            self.log.info('获取返回的协议状态码:{}'.format(status))

            return r
        except Exception as e:
            print(e)
            self.log.error('接口请求发生未知的错误:{}'.format(e))

# c = ConfigHttp()
# c.get(1)



