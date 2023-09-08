
from classes import Periodic,Processor,Aperiodic

from partition_algorithms import lbpsa,edf_ff,edf_bf

from algorithms import edf,tbs

from metric import lmse

from helper import get_tasks

import random 


def init_cores(n):
    processors = [Processor(i) for i in range(n)]
    
    return processors

def init_tasks(tasks_list):
    periodic_tasks = []
    for i in tasks_list:
        periodic_tasks.append(Periodic(i[0],i[1],i[2]))

    return periodic_tasks


periodic_tasks = init_tasks(get_tasks(1))

processors = init_cores(6)

edf_ff([i for i in periodic_tasks],processors)


util = [0 for i in range(6)]

processors.sort(key = lambda x:x.no)

aperiodic_tasks = []

#WCET_Remaining_Aperiodic = []

#WCET_Remaining_Periodic = [0] * len(periodic_tasks)

time = 0
duration = 252000


while time <= duration:

    if random.random() < 1/10000:

        aperiodic_tasks.append(Aperiodic(len(aperiodic_tasks),random.randint(100,1000),time))
        tbs(aperiodic_tasks[-1],processors)
        # WCET_Remaining_Aperiodic.append(aperiodic_tasks[-1].WCET)

        # print(f"aperiodic arrived at time {time}\n{aperiodic_tasks[-1]}")
        # print()


    for i,task in enumerate(periodic_tasks):
        if time % task.period == 0:
            if task.remaining_time:
                print(f'Task is missed at time: {time}\n{task}')
#            WCET_Remaining_Periodic[i] = task.WCET
            task.remaining_time = task.WCET



    # tasks_left = []
    # for i in range(len(periodic_tasks)):
    #     if WCET_Remaining_Periodic[i]:
    #         tasks_left.append(i)




    for i in processors:
        n = edf(i,time)
        # if n:
        #     if WCET_Remaining_Periodic[int(n.no)]:
        #         WCET_Remaining_Periodic[int(n.no)] = max(0,WCET_Remaining_Periodic[int(n.no)] - 1)   
        #         util[i.no] += 1 

        
    time += 1


