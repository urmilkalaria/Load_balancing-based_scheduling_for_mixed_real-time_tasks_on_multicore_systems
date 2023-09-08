import csv

def get_tasks(n):
	tasks = []
	with open('taskset' +str(n)  + '.csv', newline='', encoding='utf-8') as f:
		reader = csv.reader(f)
		for row in reader:
			tasks.append(row)

	return tasks