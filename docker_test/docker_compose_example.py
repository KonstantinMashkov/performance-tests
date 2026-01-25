from redis import Redis

cache = Redis(host="redis_ex", port=6379)
cache.set("example", 5)
print(int(cache.get("example")) ** 2)
