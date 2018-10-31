import redis
#http://www.cnblogs.com/melonjiang/p/5342505.html
from dev.configUtil import getPropertyVal

def RedisPool():
    pool = redis.ConnectionPool(host=getPropertyVal('redis','redis_host'), port=getPropertyVal('redis','redis_port'), db=getPropertyVal('redis','redis_db'))
    r = redis.Redis(connection_pool=pool)
    return r

def setHashVal(name, key, value):
    rd=RedisPool()
    rd.hset(name, key, value)


def getHashVal(name):
    rd=RedisPool()
    return rd.hgetall(name)
