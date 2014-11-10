import random,time,os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

while True:
  q = "%s %s %s" % (random.choice(range(10)), random.choice(['+','-']),random.choice(range(10)))
  print q, '='
  a = raw_input()
  r = eval(q)
  try:
    n = int(a)
  except:
    n = None

  if n == r:
    print bcolors.OKGREEN+"Correct!"+bcolors.ENDC
  else:
    print bcolors.FAIL+"Wrong: %s = %d" % (q,r) + bcolors.ENDC
  time.sleep(1)
   
