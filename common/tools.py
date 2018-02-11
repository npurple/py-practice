from __future__ import print_function
import sys

def p(*args, **kargs):
    try:
        print(*args, sep=' ', end='\n', file=sys.stdout, flush=False)
    except:
        print(*args, sep=' ', end='\n', file=sys.stdout)

