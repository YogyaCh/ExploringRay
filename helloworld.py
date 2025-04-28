import ray

# Stateless task run on a remote worker
@ray.remote
def square(x):
    return x * x

ray.init()

# futures is a promise that these will run in parallel when called
futures = [square.remote(i) for i in range(4)]

print(ray.get(futures))
