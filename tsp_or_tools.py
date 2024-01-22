

from __future__ import print_function
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import numpy as np
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math
import time
import matplotlib.pyplot as plt

import pickle

scale=10000000

num_samples=100
size=2000

filename='tsp_{}_{}.pkl'.format(size,num_samples)
with open(filename,'rb') as f:
    data1=pickle.load(f)
print(len(data1))

def distance_matrix(loc):
    return np.sqrt(np.sum((loc[:,None,:]-loc[None,:,:])**2,-1))


def create_data_model(loc):
    """Stores the data for the problem."""
    data = {}
    data['distance_matrix'] = distance_matrix(loc*scale)  # yapf: disable
    data['num_vehicles'] = 1
    data['depot'] = 0
    return data


def print_solution(manager, routing, solution):
    """Prints solution on console."""
#     print('Objective: {} miles'.format(solution.ObjectiveValue()))
    index = routing.Start(0)
#     plan_output = 'Route for vehicle 0:\n'
    route_distance = 0
    while not routing.IsEnd(index):
#         plan_output += ' {} ->'.format(manager.IndexToNode(index))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
#     plan_output += ' {}\n'.format(manager.IndexToNode(index))
#     print(plan_output)
#     plan_output += 'Route distance: {}miles\n'.format(route_distance)
    return route_distance


def main(n):
    """Entry point of the program."""
    # Instantiate the data problem.
    data = create_data_model(data1[n])

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                           data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)


    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if solution:
        return print_solution(manager, routing, solution)


if __name__ == '__main__':
    t=0
    cost=[]
    for n in range(100):
        t1=time.time()
        cc=main(n)/scale
        cost.append(cc)
        t2=time.time()
        print('{},cost={},time={}'.format(n,cc,t2-t1))
        t=t2-t1+t
    print('avg time=',t/100)
    print('avg cost=',sum(cost)/100)