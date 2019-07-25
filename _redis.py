# to check a global flag in redis

import redis

r = redis.Redis(host='localhost', port=6379, db=0)

while r.get('foo') is not True:
    print('runnin...')
