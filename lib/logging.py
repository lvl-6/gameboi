###############################################################################
#
# Description:
# A simple output formatter for logging messages.
# Only using this because I cba with Python's own logging module right now.
#
###############################################################################

from datetime import datetime


def print_log(message: str):
    """Print logging messages with a timestamp"""
    d = datetime.now()

    timestamp = (
        str(d.day) + '/'
        + str(d.month) + '/'
        + str(d.year)
        + ' @ '
        + str(d.hour) + ':'
        + str(d.minute) + ':'
        + str(d.second)
        )

    print('['+timestamp+']' +' '+  message)
