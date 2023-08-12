timer = 0
import time
secs = int(input("몇초 셀지\n"))
for i in range(1, secs +1):
    time.sleep(1)
    print(i)