import os
import json
import time
from app import create_redis_instance


class RedisService:
    POOL_KEY = os.getenv("REDIS_IDS_POOL_KEY")

    @staticmethod
    def pick_id() -> str:
        redis = create_redis_instance()

        failed_tries = 0
        while failed_tries < 5:
            if redis.exists(RedisService.POOL_KEY):
                pool = json.loads(redis.get(RedisService.POOL_KEY))
                if len(pool) > 0:
                    item = pool[0]
                    redis.set(RedisService.POOL_KEY, json.dumps(pool[1:]))
                    return item

            failed_tries += 1
            time.sleep(1)

        raise ValueError("no empty ids in redis")
