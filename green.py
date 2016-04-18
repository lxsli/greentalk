import sys
import eventlet
eventlet.monkey_patch()

def prn(*a):
    for c in a:
        sys.stdout.write(c)

h = eventlet.spawn(prn, 'Hello,')
w = eventlet.spawn(prn, ' world!')
h.wait()
w.wait()
