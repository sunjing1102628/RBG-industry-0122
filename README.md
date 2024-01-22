```bash

# To train the model on different sizes, use the commands:

##500
python region_vrp.py --epoch_size 100 --save_epoch 5 --num_epochs 100 --batch_size 14 --size 500 --near_K 5 --val_size 20 --model_type 1 --update_model_step 12 --enable_gradient_clipping --enable_random_rotate_train --enable_random_rotate_eval --up_rate_train 0.005 --up_rate_eval 0.0005 --rl_steps 1 --eval_batch_size 20 --lr1 3e-5 --lr2 1e-3 --enable_running_cost --fix_select_model


## 1000
python region_vrp.py --epoch_size 50 --save_epoch 5 --num_epochs 100 --batch_size 6 --size 1000 --near_K 8 --val_size 20 --model_type 1 --update_model_step 12 --enable_gradient_clipping --enable_random_rotate_train --enable_random_rotate_eval --up_rate_train 0.005 --up_rate_eval 0.0005 --rl_steps 1 --eval_batch_size 20 --lr1 3e-5 --lr2 1e-3 --enable_running_cost --fix_select_model

## 2000
python region_vrp.py --epoch_size 25 --save_epoch 5 --num_epochs 100 --batch_size 2 --size 2000 --near_K 9 --val_size 20 --model_type 1 --update_model_step 12 --enable_gradient_clipping --enable_random_rotate_train --enable_random_rotate_eval --up_rate_train 0.005 --up_rate_eval 0.0005 --rl_steps 1 --eval_batch_size 20 --lr1 3e-5 --lr2 1e-3 --enable_running_cost --fix_select_model

# to evaluate, run the eval() function in region_vrp.py

```

