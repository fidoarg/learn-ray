import ray

import time
import logging

logger = logging.getLogger(__name__)
ray.init()

@ray.remote
class Counter:
    def __init__(self) -> None:
        self.value = 0

    def increment(self):
        self.value += 1
        return self.value

    def get_counter(self):
        return self.value
    
counter : Counter = Counter.remote()
obj_ref = counter.increment.remote()

list_counters = [Counter.remote() for _ in range(10)]
list_obj_ref = [list_counters[idx].increment.remote() for idx in range(10)]
list_obj_ref_2 = [list_counters[0].increment.remote() for idx in range(10)]


print(ray.get(list_obj_ref))
print(ray.get(list_obj_ref_2))
