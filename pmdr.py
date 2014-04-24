#!/usr/bin/env python

import time
import sys


def timer(minute):
    """
    Calling this function will generate a timer for the given minutes and
    wait until it finishes. It'll also generate a printable timer.
    """
    start_time = time.time()
    end_time = start_time + (minute * 60)
    while time.time() < end_time:
        clock = time.strftime("%H:%M:%S", time.localtime(time.time()))
        sys.stdout.write("%s    \r" % (clock))
        sys.stdout.flush()


timer(1)
