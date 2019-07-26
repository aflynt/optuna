#!/usr/bin/python
import optuna
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import rhino3dm
import sys
import subprocess

# global variable works
sn = 'sgmr' # study name
studyloc = 'sqlite:///sgmr.db' # database
nt = 300 # number of trials

def objective(trial):
    # suggest variables
    LCR  = 6.0
    Hin  = 3.0
    Hout = 1.0
    x1 = trial.suggest_uniform( 'x1',  0.02 * LCR, 1.0*LCR/3.0 - 1e-6)
    x2 = trial.suggest_uniform( 'x2', 1.0*LCR/3.0, 2.0*LCR/3.0 - 1e-6)
    x3 = trial.suggest_uniform( 'x3', 2.0*LCR/3.0, 0.98*LCR)
    y2 = trial.suggest_uniform( 'y2', Hout, Hin)

    # make list of 5 points to create nurbs curve
    pList = rhino3dm.Point3dList()
    pList.Add(0.0, Hin,0)
    pList.Add(x1 , Hin,0)
    pList.Add(x2 ,  y2,0)
    pList.Add(x3 ,Hout,0)
    pList.Add(6.0,Hout,0)
    nc = rhino3dm.NurbsCurve.Create(False, 3, pList)

    # files to write curves to
    fy = open('fy_curve.csv', 'w')
    fz = open('fz_curve.csv', 'w')

    # write curves to file
    for n in range(101):
      pt = nc.PointAt(2*n/100.0).Encode()
      fy.write("{},{},{}\n".format(pt['X'], pt['Y'],     0.0))
      fz.write("{},{},{}\n".format(pt['X'],     0.0, pt['Y']))
    fy.close()
    fz.close()

    # write case number to file
    with open('prob_num', 'w') as wf:
      wf.write(str(trial.number))

    # run ccm+ process
    outfile = open('result.txt', 'w')
    cp = subprocess.run(["runf"], stdout=outfile )
    outfile.close()

    # read file to get objective value
    resfile = 'last_obj_table_300.csv'
    cp = subprocess.run(["tail", "-n", "1", resfile ], stdout=subprocess.PIPE )
    value = str(cp.stdout, 'utf-8').rstrip()
    result = [x.strip() for x in value.split(',')][0]
    result = float(result)

    # copy results for saving
    outf = 'trial'+str(trial.number)+'_data.csv'
    cp = subprocess.run(["cp", resfile, outf ], stdout=subprocess.PIPE )

    return result

study = optuna.create_study(study_name=sn, storage=studyloc, load_if_exists=True)
study.optimize(objective, n_trials=nt)


print('\n=== dataframe   ===')
df = study.trials_dataframe()
print(df)

vals = df.values

# trial num
print(vals[:,0])

# trial vals
tv = vals[:,2]
z = tv.tolist()
#print(tv)

# params
x1 = vals[:,5]
x2 = vals[:,6]
x3 = vals[:,7]
y2 = vals[:,8]

# make scatter plot
fig, ax = plt.subplots()
scatter = ax.scatter(x1, x2, c=z, s=z, cmap="Spectral")
ax.set(xlabel='x1', ylabel='x2',title='Trial Results')
ax.grid()
plt.show()


# make regular plots
plt.subplot(4,1,1)
plt.plot(x1, z, 'r.')
plt.title('Trial Results')
plt.ylabel('Z vs x1')
plt.grid()

plt.subplot(4,1,2)
plt.plot(x2, z, 'b.')
plt.xlabel('parameters')
plt.ylabel('Z vs x2')
plt.grid()

plt.subplot(4,1,3)
plt.plot(x3, z, 'g.')
plt.xlabel('parameters')
plt.ylabel('Z vs x3')
plt.grid()

plt.subplot(4,1,4)
plt.plot(y2, z, 'm.')
plt.xlabel('parameters')
plt.ylabel('Z vs y2')
plt.grid()

plt.show()


print('\n=== best_params ===')
print(study.best_params)

print('\n=== best_value  ===')
print(study.best_value)

print('\n=== best_trial  ===')
print(study.best_trial)

#print('\n=== trials      ===')
#print(study.trials)
#
#study_summaries = optuna.get_all_study_summaries(studyloc)
