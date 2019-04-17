class ExcelVariable:

    URL = 0
    headers = 1
    data = 2
    Expect = 3
    Result = 4

def getUrl():
    return ExcelVariable.URL

def getHeaders():
    return ExcelVariable.headers

def getData():
    return ExcelVariable.data

def getExpect():
    return ExcelVariable.Expect

def getResult():
    return ExcelVariable.Result

