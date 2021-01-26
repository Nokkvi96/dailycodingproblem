import time

class Hit_Counter:
    def __init__(self):
        self.hits = []

    def record(self, timestamp):
        self.hits.append(timestamp)
    
    def total(self):
        return len(self.hits)

    def range(self, lower, upper):
        inrange = []
        for i in range(0, len(self.hits)):
            if (self.hits[i] >= lower):
                for j in range(i, len(self.hits)):
                    if (self.hits[j] <= upper):
                        inrange.append(self.hits[j])
                    else: return inrange
        return inrange
    
tslist = []
ht = Hit_Counter()
for i in range(0,10):
    ts = time.time()
    tslist.append(ts)
    ht.record(ts)
print(ht.total())
print(ht.range(tslist[3],tslist[5]))