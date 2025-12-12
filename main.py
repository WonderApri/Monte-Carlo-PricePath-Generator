import numpy as np
import pandas as pd

S_value = 100        #price of asset in GBP
mu = 0.05            #annual drift (return expected)
sigma = 0.2          #annual volatility
T = 1.0              #total time in yrs
steps = 252          #steps in simulation (days in year when market open- trading year)
paths = 10000        #no. of independent price paths to simulate

dt = T / steps           
Z = np.random.normal(0,1, (paths, steps))   #produces matrix 
#each row of matrix is one price path's random noises

S = np.zeros((paths, steps + 1))
S[:, 0] = S_value
#empty matrix to hold values

for t in range(steps):
    S[:, t+1] = S[:, t] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z[:, t])
#iterates and updates all 10,000 prices simultaneously 

columns = [f"t{i}" for i in range(S.shape[1])]
df = pd.DataFrame(S, columns=columns)
df.to_csv("Monte-Carlo-Paths.csv", index=False)

print("Saved paths to Monte-Carlo-Paths.csv")