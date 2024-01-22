from torch.utils.data import Dataset
import torch
import os
import time
import pickle
import numpy as np
import argparse

from problems.vrp.state_cvrp import StateCVRP
from problems.vrp.state_sdvrp import StateSDVRP
from utils.beam_search import beam_search
from utils import generate_vrp_regions,K_means
import tqdm




if __name__=='__main__':
    parser = argparse.ArgumentParser(
        description="Attention based model for solving the Travelling Salesman Problem with Reinforcement Learning")
    parser.add_argument('--graph_size', type=int, default=500, help="The size of the problem graph")
    parser.add_argument('--K', type=int, default=5, help='Number of instances per batch during training')
    parser.add_argument('--num_samples', type=int, default=12000, help='Number of instances per epoch during training')
    parser.add_argument('--filename', type=str, default=None, help='Dataset file')
    parser.add_argument('--step', type=int, default=10)
    parser.add_argument('--beta', type=float, default=0)
    parser.add_argument('--batch_size', type=int, default=1)
    CAPACITIES=50
    
    
    opts = parser.parse_args()
    print('K=',opts.K,',graph_size=',opts.graph_size)
    
    data=[]
    for i in (range(opts.num_samples)):
        if i%50==0:
            print('{},'.format(i))
            
        data.append(generate_vrp_regions(batch_size=opts.batch_size,size=opts.graph_size,K=opts.K,center_depot=True,step=opts.step,beta=opts.beta,device=torch.device('cpu')))
    
    with open(opts.filename,'wb') as f:
        pickle.dump(data,f)
    

    