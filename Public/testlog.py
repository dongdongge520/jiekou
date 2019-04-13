from Public.log import MyLog

log=MyLog('test')
try:
    log.info('开始测试')
    r = 10/0
    log.info("resuit:"+str(r))
except ZeroDivisionError as e:
    log.error('报错信息:'+str(e))
log.info('end')