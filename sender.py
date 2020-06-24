# This will put some data in the queue.
from redis import Redis
from rq import Queue
from worker_function import worker_function

european_cities = ["Berlin", "Paris", "London", "Rome", "Warsaw", "Krakow", "Turin"]

q = Queue('cities', connection=Redis())
for some_data in european_cities:
    q.enqueue(worker_function, some_data)

