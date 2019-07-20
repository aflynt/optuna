#!/usr/bin/python
import optuna
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

sn = 'bowl-study' # study name
studyloc = 'sqlite:///bs.db' # database
nt = 10  # number of trials

def objective(trial):
    x = trial.suggest_uniform('x',-10,10)
    y = trial.suggest_uniform('y',-10,10)
    return (x-2)**2 + (y-1)**2


#study = optuna.create_study(study_name=sn, storage=studyloc)
study = optuna.create_study(study_name=sn, storage=studyloc, load_if_exists=True)
#study.optimize(objective, n_trials=nt)




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
x = vals[:,5]
print(x)

y = vals[:,6]
print(y)

# make scatter plot
fig, ax = plt.subplots()
scatter = ax.scatter(x, y, c=z, s=z, cmap="Spectral")
ax.set(xlabel='x', ylabel='y',title='Trial Results')
ax.grid()
plt.show()


# make regular plots
plt.subplot(2,1,1)
plt.plot(x, z, 'r.')
plt.title('Trial Results')
plt.ylabel('Z vs X')
plt.grid()

plt.subplot(2,1,2)
plt.plot(y, z, 'b.')
plt.xlabel('parameters')
plt.ylabel('Z vs Y')
plt.grid()

plt.show()



#plt.plot(x, tv, 'rs', y, tv, 'b^')
#plt.show()




print('\ntrue best value is = {}, {}\n'.format(2, 1))

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
