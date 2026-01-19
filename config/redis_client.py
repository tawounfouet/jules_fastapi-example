import redis
from config.settings import settings

def get_redis_client():
    """
    Creates and returns a Redis client.
    """
    client = redis.Redis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        decode_responses=True
    )
    return client

# Global instance if needed, or use dependency injection in routes
redis_client = get_redis_client()
