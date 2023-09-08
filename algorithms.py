import math


from classes import Periodic,Processor,Aperiodic
#Algorithms
#Earliest Deadline First


def edf(processor,time): 
	mi = [float('inf'),None]
	for j in processor.ptasks:
		if j.period - time % j.period < mi[0] and j.remaining_time > 0:
			mi[0] = j.period - (time % j.period) 
			mi[1] = j 
	for j in processor.atasks:
		if j.virtual_deadline - time < mi[0] and j.remaining_time > 0:
			mi[0] = j.virtual_deadline - time
			mi[1] = j

	if mi[1]:
		#print(mi[1])
		mi[1].remaining_time -= 1
		if isinstance(mi[1],Aperiodic):
			if mi[1].remaining_time == 0:	
				print(f"Aperiodic task: {mi[1]}\nDone at: {time}\n\n")
			if (mi[1].response_time) == -1:
				mi[1].response_time = time - mi[1].arrival_time
		#print(mi[1])

	return mi[1]


#Total Bandwidth Server
def tbs(aperiodic,processors):
	mi = [float('inf'),None]
	for i in processors:
		mx = 0
		for j in i.atasks:
			mx = max(mx,j.virtual_deadline)
		if i.ut() == 1:
			continue
		v = math.ceil(max(aperiodic.arrival_time,mx)+ (aperiodic.WCET/(1 - i.ut())))
		if v < mi[0]:
			mi[0] = v
			mi[1] = i

	mi[1].atasks.append(aperiodic)
	


	aperiodic.virtual_deadline = mi[0]


