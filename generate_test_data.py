def generate_test_data(path="./", device=torch.device('cpu')):
    path = 'VRP_Instances_Soloman/SenseTime_instance_1.txt'
    file = open(path, "r")
    lines = [ll.strip().split("\n") for ll in file]

    dimension0 =[]
    demand0=[]
    location0=[]
    for j in range(10, len(liness)):
        line = lines[j][0]

        clean_data = line.split()
        converted_values = [int(value) for value in clean_data]
        #print('clean data is',converted_values)
        dimension = int(converted_values[0])
        dimension0.append(dimension)

        demands = int(converted_values[3])

        demand0.append(demands)
        locationx = int(converted_values[1])
        locationy = int(converted_values[2])
        locations = [locationx, locationy]
        location0.append(locations)
    original_locations = location0
    #print('loc_type is', type(original_locations))


    #print('teat1&&&&', np.max(original_locations, axis=0))
    #print('teat2#######', np.min(original_locations, axis=0))
    max_range = np.max(original_locations, axis=0) - np.min(original_locations, axis=0)
    #print('test1$$$$$$$',max_range)
    max_range = np.max(max_range)

    if max_range < 100:
        max_range = 100
    #print(f'max_range:{max_range}')
    # Normalize the coordinates
    xys = (original_locations - np.min(original_locations, axis=0)) / max_range
    #print('final^^^^^^^^',xys)
    capacity = 1000
    node_demand = torch.Tensor(demand0) / capacity  # [1, n]
    #print('node_demand^^^^^^^',node_demand.size()
    #node_demand0 = node_demand.squeeze(0).t()

    start_time = time.time()
    #init_routes = solve_init(xys, demands, args, capacity=capacity, ptype=ptype)
    #p = VRFullProblem(xys, demands, capacity, init_routes)

    '''print('data&&&&',[{'depot': torch.tensor([0.5, 0.5]), 'loc': torch.FloatTensor(size, 2).uniform_(0, 1),
             'demand': (torch.FloatTensor(size).uniform_(0, 9).int() + 1).float() / CAPACITIES} for i in
            range(num_samples)])'''
    loc0 =torch.tensor(xys)

    return [{'depot': torch.tensor([0.5, 0.5]), 'loc': loc0.to(torch.float32),
             'demand':  node_demand}]s