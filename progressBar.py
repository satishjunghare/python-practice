import time
import sys
import click

def roomsImport():
    time.sleep(1)
    yield 30

    time.sleep(1)
    yield 70

    time.sleep(1)
    yield 100

def hotelImport():
    time.sleep(1)
    yield 10

    time.sleep(1)
    yield 40

    time.sleep(1)
    yield 50

    time.sleep(1)
    yield 80

    time.sleep(1)
    yield 100

def progress_bar(iteration, total, prefix='', suffix='', length=30, fill='█', print_end='\r'):
    """
    Print a progress bar to the console.
    
    Parameters:
    - iteration: Current iteration (int)
    - total: Total iterations (int)
    - prefix: Prefix string (str)
    - suffix: Suffix string (str)
    - length: Length of the progress bar in characters (int)
    - fill: Fill character for the progress bar (str)
    - print_end: End character for the print statement (str)
    """
    percent = f'{100 * (iteration / float(total)):.1f}'
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=print_end)
    
processes = [{"fun": "roomsImport", "prefix":"Importing rooms"}, {"fun": "hotelImport", "prefix":"Importing hotels"}]

inputTxt = input("Do you want to import data?(y/n):")
if inputTxt == "y":
    print("Proceed to import data")
else:
    print("Exiting...")
    sys.exit()

for process in processes:
    funName = process['fun']
    callFuntion = globals()[funName]

    for i in callFuntion():
        progress_bar(i, 100, prefix= process['prefix'] + ':', suffix='Complete')
    print()

print("Syncing Complete!")