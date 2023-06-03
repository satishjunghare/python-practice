import time
import sys
import click

def yieldfun():
    time.sleep(1)
    yield 100

    time.sleep(1)
    yield 100

    time.sleep(1)
    yield 1000

    time.sleep(1)
    yield 100000

    time.sleep(2)
    yield 1000000

# with click.progressbar(range(1000000)) as bar:
#     for i in bar:
#         time.sleep(0.1)
#         pass

with click.progressbar(all_the_users_to_process) as bar:
    for user in bar:
        modify_the_user(user)