import random,time,os

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
    print "Correct!"
  else:
    print "Wrong: %s = %d" % (q,r) 
  time.sleep(1)
   
