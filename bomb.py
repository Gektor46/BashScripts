import os
import time

i = 0
while True: 
  i = i + 1
  time.sleep(1)
  print(i)
  os.fork()