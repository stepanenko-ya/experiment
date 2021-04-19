import datetime
import time

start = int(datetime.datetime.now().strftime("%H%M%S"))
time.sleep(1)
stop = int(datetime.datetime.now().strftime("%H%M%S"))
print(stop - start)
