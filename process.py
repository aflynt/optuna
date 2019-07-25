#!/usr/bin/python
import subprocess


#cp = subprocess.run(["ls", "-l"], stdout=subprocess.PIPE )
#cp = subprocess.run(["add", "1", "2"], stdout=subprocess.PIPE )

#outfile = open('result.txt', 'w')
#cp = subprocess.run(["mult", "1", "2"], stdout=outfile )
#outfile.close()

#print(cp.args)
#print(cp.returncode)

#encoding = 'utf-8'
#value = cp.stdout.decode()
#value = str(cp.stdout, encoding).rstrip()
#print( value )

#prob_num = 1
#
#prob_num += 1
## write the problem number to file
#with open('prob_num', 'w') as wf:
#  wf.write(str(prob_num))
#
#with open('result.txt', 'r') as rf:
#  res = rf.read().rstrip()
#  print('I got result: '+res)

# global variable works
'''
prob_num = 0

for x in range(1,9):

  prob_num += 1
  with open('prob_num', 'w') as wf:
    wf.write(str(prob_num))

  sx = str(x)
  outfile = open('result.txt', 'w')
  cp = subprocess.run(["mult", sx, sx], stdout=outfile )
  outfile.close()

  with open('result.txt', 'r') as rf:
    res = rf.read().rstrip()
    print("Value [{}] gave result [{}]".format(x,res))

'''

# yes CCM+ script file does run in pwd
#outfile = open('result.txt', 'w')
#cp = subprocess.run(["runf"], stdout=outfile )
#outfile.close()

cp = subprocess.run(["tail", "-n", "1", "last_obj_table_300.csv" ], stdout=subprocess.PIPE )
value = str(cp.stdout, 'utf-8').rstrip()
result = [x.strip() for x in value.split(',')][0]
result = float(result)
print( result )







