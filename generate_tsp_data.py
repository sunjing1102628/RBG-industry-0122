
import numpy as np
import pickle

np.random.seed(100) 

num_samples=100
size=500

filename='tsp_{}_{}.pkl'.format(size,num_samples)
print(filename)

sizes=[500,1000,2000]
for size in sizes:
    filename='tsp_{}_{}.pkl'.format(size,num_samples)
    print(filename)
    data = [np.random.rand(size,2)
            for i in range(num_samples)
    ]
    with open(filename,'wb') as f:
        pickle.dump(data,f)