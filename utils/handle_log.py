import logging
import logging.handlers



class HandleLog:
    def __init__(self):
        # 创建一个同城游的日志器
        self.logger = logging.getLogger("tcyapp_logger")
        # 创建处理器handler_t，输出到控制台
        self.handler_t = logging.StreamHandler()
        # 创建处理器handler_f，输出到文件，切割方式：按天输出到.log文件，备份14天
        self.handler_f = logging.handlers.TimedRotatingFileHandler(r"E:\code\Python\Study\tcyapp_android\log\Tcyapp_log.log",when="Midnight",interval=1,backupCount=14,encoding="utf-8")
        # 创建格式器，格式为：
        self.fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] [%(funcName)s]  -  %(message)s"
        self.formatter = logging.Formatter(fmt=self.fmt)

    # 将msg日志信息输出到控制台
    def log_to_terminal(self,msg):
        # 设置日志器的日志级别
        self.logger.setLevel(logging.DEBUG)
        # 设置handler_t处理器的日志级别，非必须
        self.handler_t.setLevel(logging.DEBUG)
        # 添加格式器到处理器中
        self.handler_t.setFormatter(self.formatter)
        # 添加处理器到日志器中
        self.logger.addHandler(self.handler_t)
        # 输出日志
        self.logger.debug(msg)

    # 将msg日志信息输出到.log文件
    def log_to_logfile(self,msg):
        # 设置日志器的日志级别
        self.logger.setLevel(logging.INFO)
        # 设置handler_t处理器的日志级别，非必须
        self.handler_f.setLevel(logging.INFO)
        # 添加格式器到处理器中
        self.handler_f.setFormatter(self.formatter)
        # 添加处理器到日志器中
        self.logger.addHandler(self.handler_f)
        # 输出日志
        self.logger.info(msg)

    # 将日志同时输出到控制台和.log文件
    def log_to_terminal_and_logfile(self,msg):
        # 设置日志器的日志级别
        self.logger.setLevel(logging.INFO)
        # 设置处理器的日志级别，非必须
        self.handler_t.setLevel(logging.DEBUG)
        self.handler_f.setLevel(logging.INFO)
        # 添加格式器到处理器中
        self.handler_t.setFormatter(self.formatter)
        self.handler_f.setFormatter(self.formatter)
        # 添加处理器到日志器中
        self.logger.addHandler(self.handler_t)
        self.logger.addHandler(self.handler_f)
        # 输出日志
        self.logger.info(msg)




if __name__ == '__main__':
    # HandleLog().log_to_terminal("这是一条日志信息")
    # HandleLog().log_to_logfile("这是一条日志信息")
    HandleLog().log_to_terminal_and_logfile("输出到两个地方")