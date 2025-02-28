#YOUR NAME AND YOUR PARTNER'S NAME GOES HERE
#NIMA AND PEARCE
#THE NAME OF THE ALGORITHM GOES HERE
#Priority
#CLASSES GO HERE
class Process:
    def __init__(self,priority,burst_time):
        self.priority= priority
        self.burst_time= burst_time

    def __str__(self):
        return f"This process has a priority of {self.priority} and a Burst time of {self.burst_time}"

    def __lt__(self, other):
        if not isinstance(other,Process):
            return NotImplemented
        return self.priority < other.priority 


class CustomQueue:
    def __init__(self):
        self.queue=[]

    def put(self,process):
        self.queue.append(process)

    def get(self):
        if len(self.queue)>=1:
            return self.queue.pop(0)
        return None
    def __lt__(self,other):
        pass
        


class CustomScheduler:
    def schedule(self):
        pass

    def consume(self):
        pass

if __name__ == '__main__':
#REMOVE PASS AND DEMONSTRATE THE SCHEDULER IN ACTION HERE
#CREATE ANY QUEUES, PROCESSES, CALL APPROPRIATE METHODS
    pass 