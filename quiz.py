import random,time,os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

while True:
  lhs = random.choice(range(7))
  rhs = random.choice(range(6))
  op  = random.choice(['+','-']) 
  q = "%s %s %s " % (lhs, op, rhs)
  r = eval(q)
  qa =  random.choice([0,1])
  compare_result, compare_lhs = False, False
  if qa == 0:
    qa = random.choice([0,1])
    if qa == 0:
      compare_lhs = True
      q = "%s %s %s = %s" % ('_',op,rhs,r)
    else:
      q = "%s %s %s = %s" % (lhs,op,'_',r)
  else:
    q += " ="
    compare_result = True
  print q
  a = raw_input()
  try:
    n = int(a)
  except:
    n = None

  answer_ok = False
  if not compare_result:
   if compare_lhs:
     q2 = "%s %s %s" % (n,op,rhs)
     r2 = eval(q2)
   else:
     q2 = "%s %s %s" % (lhs,op,n)
     r2 = eval(q2)
   answer_ok = r2 == r
  else:
     answer_ok = n == r  
  if answer_ok:
    print bcolors.OKGREEN+"Correct!"+bcolors.ENDC
  else:
    print bcolors.FAIL+"Wrong: %s %s %s = %d" % (lhs, op, rhs, r) + bcolors.ENDC
  time.sleep(0.5)
   
