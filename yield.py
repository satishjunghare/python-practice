"""
The yield statement suspends a function’s execution and sends a value back to the caller, 
but retains enough state to enable the function to resume where it left off. 
When the function resumes, it continues execution immediately after the last yield run. 
This allows its code to produce a series of values over time, 
rather than computing them at once and sending them back like a list.
"""

import time

def anotherFun():
    time.sleep(1)
    return "-------"

def yieldfun():
    time.sleep(1)
    yield "-------"

    time.sleep(1)
    yield "-------"

    time.sleep(1)
    yield "-------"

    time.sleep(1)
    yield "-------"

    time.sleep(1)
    yield "-------"

    yield anotherFun()


yieldfundata = yieldfun()
for f in yieldfundata:
    print(f)