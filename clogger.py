import time
from os import path

CLOGGER = "clogger"
LOG_INFO = "INFO"
LOG_WARNING = "WARNING"
LOG_ERROR = "ERROR"
LOG_DATA = "DATA"
LOG_PROCESS = "PROCESS"


# TODO this needs some try except and if statements to ensure it doesn't cause errors.
class Clogger:
    """Custom logger because ESRI is also logging and this interferes with standard logging."""
    def __init__(self, logfile_path):
        self.f_name_append = time.strftime('%Y%m%d_%H%M%S')
        self.logfile_path = logfile_path,
        self.logfile = f"{CLOGGER}_{self.f_name_append}.log"
        self.file = open(path.join(self.logfile_path[0], self.logfile), "w")
        self.file.write(f"TIME|PRIORITY|MESSAGE\n")
        self.file.close()

    def write_line(self, items):
        self.file = open(path.join(self.logfile_path[0], self.logfile), "a")
        time_obj = time.gmtime()
        try:
            self.file.write(f"{time.asctime(time_obj)}|{items[0]}|{items[1]}\n")
        except Exception as e:
            self.file.write(f"{time_obj}|{LOG_ERROR}|{e}\n")
        self.file.close()

    def info(self, log_item):
        self.write_line([LOG_INFO, log_item])

    def data(self, log_item):
        self.write_line([LOG_DATA, log_item])

    def process(self, log_item):
        self.write_line([LOG_PROCESS, log_item])

    def warning(self, log_item):
        self.write_line([LOG_WARNING, log_item])

    def error(self, log_item):
        self.write_line([LOG_ERROR, log_item])

    def shut_down_logger(self):
        self.file.close()
