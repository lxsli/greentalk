import sys
import threading

def prn(*a):
    for c in a:
        sys.stdout.write(c)

h = threading.Thread(target=prn, args=('Hello,'))
w = threading.Thread(target=prn, args=(' world!'))
h.start()
w.start()
h.join()
w.join()
