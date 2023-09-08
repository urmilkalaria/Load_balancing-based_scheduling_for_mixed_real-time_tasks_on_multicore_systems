import random
import csv

def get_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
        
            factors.append(i)
    return factors



def generate_taskset(num_periodic,n_cores, utilisation,period_choice):
    taskset = []
    total_utilization = 0
    for i in range(num_periodic):
        load = round(random.uniform(0, 1), 2)

        period = random.choice(period_choice)

        execution_time = (period * load)
        task = (i, execution_time, period)
        taskset.append(task)

        total_utilization += load
    print(taskset)
    print(total_utilization)	
    target_utilization = min(n_cores * utilisation, total_utilization) 
    if(target_utilization < total_utilization):
        adjustment_factor = target_utilization / total_utilization
    else:
        adjustment_factor = 1
    
    for i in range(num_periodic):
        task = taskset[i]
        load = task[1] / task[2]

        taskset[i] = (task[0], round((task[1] * adjustment_factor),0), task[2])


    periodic_util = sum([i[1]/i[2] for i in taskset])
    print(periodic_util)

    return taskset


n = generate_taskset(25,6,0.5,[100 * i for i in range(1,11)])

# n = np.array(n)

# print(n)
def write(taskset,no):
    with open('taskset' + str(no) + '.csv','w',newline='') as file:
        writer = csv.writer(file)
        for task in taskset:
            print(task)
            writer.writerow(task)

write(n,1)
# print(n)

def generate_multiple_tasksets(offset , num_sets, num_tasks, n_cores, l_util, h_util):
    all_tasksets = []
    for i in range(num_sets):
        with open("taskset" + str(int(offset + i)) + ".csv", 'w', newline='') as file:
                writer = csv.writer(file)
                taskset = generate_taskset(num_tasks, n_cores, l_util, h_util)[0]
                writer.writerow(list(task) for task in taskset)
    return all_tasksets


