

import time


timestamp = time.time()

print("Seconds since January 1, 1970:", "{:,.4f}".format(timestamp), "or", "{:.2e}".format(timestamp), "in scientific notation")

print(time.strftime("%b %d %Y", time.localtime(timestamp)))

