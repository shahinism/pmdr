#!/usr/bin/env python

import time
import sys


def timer(minute):
    """
    Calling this function will generate a timer for the given minutes and
    wait until it finishes. It'll also generate a printable timer.
    """
    end_time = time.time() + (minute * 60)
    while time.time() < end_time:
        clock = time.strftime("%H:%M:%S", time.localtime(time.time()))
        sys.stdout.write("%s    \r" % (clock))
        sys.stdout.flush()


def calltimer(status, pmdrtime=25, resttime=5, longrest=25):
    """
    Call timer based on status which can be in 3 types: pomodoro, rest,
    longrest.
    """
    if status == "pomodoro":
        timer(pmdrtime)
    elif status == "rest":
        timer(resttime)
    else:
        timer(longrest)
