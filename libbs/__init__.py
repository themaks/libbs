__version__ = "1.2.7"

import logging
logging.getLogger("libbs").addHandler(logging.NullHandler())
from libbs.logger import Loggers
loggers = Loggers()
del Loggers
del logging
