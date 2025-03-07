#YOUR NAME AND YOUR PARTNER'S NAME GOES HERE
# Pearce + Nima
#THE NAME OF THE ALGORITHM GOES HERE
# Multilevel queue

#CLASSES GO HERE

class Process:
    def __init__(self, id, priority, burst_time):
        self.id = id
        self.priority = priority 
        self.burst_time = burst_time

    def __str__(self):
        return f"ID: {self.id} Priority: {self.priority} Burst: {self.burst_time}"

    def __lt__(self, other):
        return self.priority < other.priority  


class CustomQueue:
    def __init__(self, priority_level):
        self.queue = []
        self.priority_level = priority_level

    def put(self, process):
        self.queue.append(process)
        self.queue.sort()  

    def get(self):
        if self.queue:
            return self.queue.pop(0)  
        return None

    def __lt__(self, other):
        return self.priority_level < other.priority_level

    def is_empty(self):
        return len(self.queue) == 0


class CustomScheduler:
    def __init__(self):
        self.queues = [CustomQueue(priority) for priority in range(3)]  

    def schedule(self, process):
        self.queues[process.priority].put(process)
        print(f"Scheduled: {process}")

    def consume(self):
        print("\n")
        for queue in self.queues:
            while not queue.is_empty():
                process = queue.get()
                print(f"Executing: {process}")




if __name__ == '__main__':
#REMOVE PASS AND DEMONSTRATE THE SCHEDULER IN ACTION HERE
#CREATE ANY QUEUES, PROCESSES, CALL APPROPRIATE METHODS
    scheduler = CustomScheduler()
    processes = [
        Process(1, 0, 5),
        Process(2, 1, 3),
        Process(3, 2, 2),
        Process(4, 0, 4),
        Process(5, 1, 6)
    ]

    for p in processes:
        scheduler.schedule(p)

    scheduler.consume()
    