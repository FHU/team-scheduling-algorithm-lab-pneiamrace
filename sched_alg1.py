#YOUR NAME AND YOUR PARTNER'S NAME GOES HERE
#NIMA AND PEARCE
#THE NAME OF THE ALGORITHM GOES HERE
#Priority
#CLASSES GO HERE
import heapq
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
        heapq.heappush(self.queue,process)

    def get(self):
        if self.queue:
            return heapq.heappop(self.queue)
        else:
            return None
        
    def length(self):
        return len(self.queue)
        


class CustomScheduler:
    def __init__(self):
        self.process_queue= CustomQueue()

    def schedule(self,process_list):
            for process in process_list:
                self.process_queue.put(process)

    def consume(self):
        while self.process_queue.length() > 0:
            process = self.process_queue.get()
            print(f"Executing: {process}")

if __name__ == '__main__':
#REMOVE PASS AND DEMONSTRATE THE SCHEDULER IN ACTION HERE
#CREATE ANY QUEUES, PROCESSES, CALL APPROPRIATE METHODS
    processes=[
        Process(4,10),
        Process(2,5),
        Process(1,5),
        Process(5,3)
    ]
    scheduler=CustomScheduler()
    scheduler.schedule(processes)
    scheduler.consume()

