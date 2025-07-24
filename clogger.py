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
    def __init__(self, logfile_path, logfile_name=None):
        self.f_name_append = time.strftime('%Y%m%d_%H%M%S')

        if not logfile_name:
            timestamp = time.strftime('%Y%m%d_%H%M%S')
            logfile_name = f"{CLOGGER}_{timestamp}.log"

        self.logfile_path = logfile_path
        self.logfile = logfile_name
        self.file = open(path.join(self.logfile_path, self.logfile), "w")
        self.file.write(f"TIME|PRIORITY|MESSAGE\n")
        self.file.close()

    def write_line(self, level, message):
        self.file = open(path.join(self.logfile_path, self.logfile), "a")
        timestamp = time.asctime(time.gmtime())
        try:
            self.file.write(f"{timestamp}|{level}|{message}\n")
        except Exception as e:
            self.file.write(f"{timestamp}|{LOG_ERROR}|{str(e)}\n")
            self.file.close()

    def info(self, msg):
        self.write_line(LOG_INFO, msg)

    def data(self, msg):
        self.write_line(LOG_DATA, msg)

    def process(self, msg):
        self.write_line(LOG_PROCESS, msg)

    def warning(self, msg):
        self.write_line(LOG_WARNING, msg)

    def error(self, msg):
        self.write_line(LOG_ERROR, msg)

    def shut_down_logger(self):
        self.file.close()
