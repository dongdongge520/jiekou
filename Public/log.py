import logging
import time
import os
from Public.getcwd import get_cwd

class MyLog():
    def __init__(self,logger):
        """
        指定保存日志的文件路径，日志级别，以及调用文件
        将日志存入到指定的文件中
        :param logger:  定义对应的程序模块名name，默认为root
        """

        #创建一个logger
        self.logger=logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG) # 指定最低的日志级别 critical > error > warning > info > debug

        #创建日志名称
        rq=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        path=get_cwd()
        log_path=os.path.join(path,'Log/')
        log_name=log_path+rq+'.log'

        # 创建一个handler，用于写入日志文件
        fh=logging.FileHandler(log_name,encoding='utf-8')
        fh.setLevel(logging.DEBUG)

        # 再创建一个handler，用于输出到控制台
#        ch=logging.StreamHandler(log_name)
#        ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formmter=logging.Formatter('%(asctime)s -%(name)s - %(levelname)s - %(message)s ')
        fh.setFormatter(formmter)
#        ch.setFormatter(formmter)

        # 给logger添加handler
        self.logger.addHandler(fh)
#        self.logger.addHandler(ch)

    def debug(self,msg):
        """
        定义输出的颜色debug--white，info--green，warning/error/critical--red
        :param msg: 输出的log文字
        :return:
        """
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)


# log = MyLog('test')
# log.debug('debug')
# log.info('info')
# log.error('error')
# log.warning('warning')
# log.critical('critical')



