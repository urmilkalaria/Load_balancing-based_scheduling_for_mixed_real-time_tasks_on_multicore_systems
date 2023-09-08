def edf_ff(tasks,processors):
	tasks.sort(key = lambda x: x.WCET)
	i = 0
	while i < len(tasks):
		flag = True
		for j in processors:
			if(j.ut() + tasks[i].ut() <= 1):
				j.ptasks.append(tasks[i])
				tasks.pop(i)
				flag= False
				break

		if flag:
			i += 1
			
def edf_bf(tasks,processors):
	tasks.sort(key = lambda x: x.WCET)
	i = 0

	while i < len(tasks):
		processors.sort(key = lambda x: x.ut())
		flag = True
		for j in processors:
			if(j.ut() + tasks[i].ut() <= 1):
				j.ptasks.append(tasks[i])
				tasks.pop(i)
				flag = False
				break

		if flag:
			i += 1

def lbpsa(processors,k):
	avg_ult = 0
	flag = False
	for i in processors:
		avg_ult += i.ut()
		i.ptasks.sort(key = lambda x: x.ut())
	avg_ult /= len(processors)
	processors.sort(key = lambda x: x.ut())
	for i in range(len(processors)):

		for j in processors:
			j.ptasks.sort(key = lambda x: x.ut())

		if(processors[i].ut() <= avg_ult - k):
			for j in range(i + 1,len(processors)):
				if(not(processors[j].ptasks)):
					continue
				while processors[j].ut() - processors[j].ptasks[0].ut() > (avg_ult - k)  and processors[i].ut() + processors[j].ptasks[0].ut() < avg_ult:
					flag = True
					processors[i].ptasks.append(processors[j].ptasks[0])
					processors[j].ptasks.pop(0)

	if flag:
		lbpsa(processors,0.05)
