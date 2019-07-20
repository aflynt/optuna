#!/usr/bin/python
import optuna
import matplotlib.pyplot as plt

sn = 'example-study'
studyloc = 'sqlite:///example.db'
nt = 10

def objective(trial):
    x = trial.suggest_uniform('x',-10,10)
    return (x-2)**2


#study = optuna.create_study(study_name=sn, storage=studyloc)
study = optuna.create_study(study_name=sn, storage=studyloc, load_if_exists=True)
#study.optimize(objective, n_trials=nt)



print('\ntrue best value is = {}\n'.format(2))

print('\n=== dataframe   ===')
df = study.trials_dataframe()
print(df)

vals = df.values

# trial num
print(vals[:,0])

# trial vals
tv = vals[:,2]
#print(tv)

# param x
params = vals[:,5]
print(params)

plt.plot(params, tv, 'rs')
plt.show()



#print(len(df))
#print(df[0])
#for row in df:
#    print(row)
#    for j in range(len(df[i])):
#        print('var = {}\n'.format(df[i][j]))

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
