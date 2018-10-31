import redis
#http://www.cnblogs.com/melonjiang/p/5342505.html

def RedisPool():
    pool = redis.ConnectionPool(host='192.168.1.100', port=6379, db=0)
    r = redis.Redis(connection_pool=pool)
    return r

def setHashVal(name, key, value):
    rd=RedisPool()
    rd.hset(name, key, value)


def getHashVal(name):
    rd=RedisPool()
    return rd.hgetall(name)
x=getHashVal('user')
for a,b in x.items():
    print(a,b)


