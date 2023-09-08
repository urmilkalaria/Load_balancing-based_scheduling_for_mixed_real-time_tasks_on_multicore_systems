class Processor():

    def __init__(self,no):
        self.no = int(no)
        self.ptasks = []
        self.atasks = []
        self.current_task = None
    def ut(self):
        x = 0
        for i in self.ptasks:
            x += i.ut()

        for i in self.atasks:
            x += i.ut()
        return x


    def __str__(self):
        return f"Processor no: {self.no} \n Processor period tasks: {self.ptasks} \n Processor UT {self.ut()} \n Processor aperiodic tasks: {self.atasks}"


class Periodic():
    def __init__(self,no,WCET,period):
        self.period = float(period)
        self.WCET = float(WCET)
        self.remaining_time = 0
        self.no = int(no) 


    def ut(self):
        return self.WCET/self.period 

    def __str__(self):
        return f'task no: {self.no}, \ntask WCET: {self.WCET} \ntask period: {self.period} \ntask ut {self.ut()} \ntask remaining_time: {self.remaining_time}\n\n'


class Aperiodic():
    def __init__(self,no,WCET,arrival_time,virtual_deadline = float('inf')):
        self.no = int(no)
        self.WCET = float(WCET)
        self.remaining_time = float(WCET)
        self.arrival_time = float(arrival_time)
        self.virtual_deadline = virtual_deadline
        self.response_time = -1


    def ut(self):
        return self.WCET/self.virtual_deadline

    def __str__(self):
        return f'task no:{self.no}\nWCET: {self.WCET}\nArrival_time: {self.arrival_time}\nvirtual_deadline: {self.virtual_deadline}\nResponse_time: {self.response_time}'
