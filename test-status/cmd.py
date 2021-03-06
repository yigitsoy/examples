import sys
import time

with open('/envoyai/input/behavior', 'r') as f, \
        open('/envoyai/input/message', 'a') as m:
    m.write('reading behavior')
    behavior = f.read()
if behavior == 'run':
    with open('/envoyai/input/name', 'r') as f, \
            open('/envoyai/input/message', 'a') as m:
        m.write('reading name')
        name = f.read()
    # update progress by appending to file, and use time.sleep only as a demonstration
    with open('/envoyai/status/progress', 'a') as f, \
            open('/envoyai/input/message', 'a') as m:
        m.write('waiting')
        f.write("1%")
    time.sleep(7)
    with open('/envoyai/status/progress', 'a') as f, \
            open('/envoyai/input/message', 'a') as m:
        f.write("50%")
    time.sleep(7)
    with open('/envoyai/status/progress', 'a') as f, \
            open('/envoyai/input/message', 'a') as m:
        f.write("99%")
    #  read from input and write output
    with open('/envoyai/output/hello', 'w') as f, \
            open('/envoyai/input/message', 'a') as m:
        f.write(name + ', come with me if you want to live.')
    sys.exit(0)
elif behavior == 'timeout':
    with open('/envoyai/status/warn', 'w') as w, \
         open('/envoyai/input/message', 'a') as m:
        m.write('waiting')
        w.write('about to wait for two hours,\nthis execution should timeout')
    time.sleep(60 * 60 * 2)  # two hours
else:
    with open('/envoyai/status/error','w') as e, \
         open('/envoyai/input/message', 'a') as m:
        m.write('failing')
        e.write('this execution failed because it was chosen to fail')