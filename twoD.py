#!/usr/bin/python

import optuna

def objective(trial):
    x = trial.suggest_uniform('x',-10,10)
    y = trial.suggest_uniform('y',-10,10)
    z = trial.suggest_uniform('z',-10,10)
    p = trial.suggest_uniform('p',-10,10)
    return (x-2)**2+(y-3)**2+(z-4)**2 +abs(p)

study = optuna.create_study()
study.optimize(objective, n_trials=400)
study.best_params
print('actual best is: 2 3 4 0')
