import os
from region_vrp import *
models=[r for r in os.listdir('saved')]
sizes=[500,1000,2000]
ids=list(range(5,11))
num_samples=100
CAPACITY=50
seed=100
torch.manual_seed(seed)
near_Ks=[5,9,9]
datas={}
for size in sizes:
    path='data/data_{}_{}_{}.pkl'.format(size,num_samples,CAPACITY)
    with open(path,'rb') as f:
        datas[size]=pickle.load(f)

#betas=[0,0.05,0.1,0.2,0.5,1,2,5,10,10000000]
betas=[0.5,1,2,5,10,10000000]

iter_steps=[1,11,21,31]
# iter_steps=[1,2,3]
batch_sizes={500:15,1000:6,2000:2}

# record_max_epoch1=torch.zeros(len(ids),len(sizes))
record_costs1=torch.zeros(len(betas),len(sizes),len(iter_steps),100)
record_mean_cost1=torch.zeros(len(betas),len(sizes),len(iter_steps))
record_mean_time1=torch.zeros(len(betas),len(sizes))
for beta_id,beta in enumerate(betas):
    for size_id,size in enumerate(sizes):
        print('beta=',beta,'size=',size)
        torch.manual_seed(seed)
        selectmodel=SelectModel(near_K=near_Ks[size_id],device=device).to(device)
#         with open('saved/'+models[record_idx],'rb') as f:
#             a,b=pickle.load(f)
#             model.load_state_dict(a)
#             selectmodel.load_state_dict(b)
        t1=time.time()
        costs,regionss2,iter_costs=eval(datas[size],model,selectmodel,batch=batch_sizes[size],iter_step=iter_steps[-1],beta=beta,
                             K_means_step=10,always_update=False,record_iter_steps=iter_steps )
#             record_max_epoch[idx_id,size_id]=max_epoch
        record_mean_time1[beta_id,size_id]=(time.time()-t1)/100
        record_costs1[beta_id,size_id,:,:]=iter_costs
        record_mean_cost1[beta_id,size_id,:]=torch.mean(iter_costs,-1)




print(record_costs1)
#print(record_max_epoch1)
print(record_mean_time1)
print(record_mean_cost1)

with open('results2.pkl','wb') as f:
    pickle.dump([record_costs1,record_mean_time1,record_mean_cost1],f)
