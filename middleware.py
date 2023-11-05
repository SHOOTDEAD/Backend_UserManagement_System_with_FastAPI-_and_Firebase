# Store request timestamps and counters for rate limiting
request_history = {}
rate_limit = 10  # number of requestspermitted
time_limit = 60  # time limit in seconds
from functools import wraps
from datetime import datetime, timedelta
from fastapi import HTTPException


def rate_limit(limit: int, window: int):
    """
    Limits the number of requests sent to the api per user

    :param limit : number request permitted
    :param window : Time window

    :raise : HTTPException
    """

    def decorator(func):
        @wraps(func)
        async def wrapper(request, *args, **kwargs):
            now = datetime.utcnow()
            ip_address = request.client.host

            if ip_address not in request_history:
                request_history[ip_address] = []

            request_history[ip_address] = [
                timestamp
                for timestamp in request_history[ip_address]
                if now - timestamp < timedelta(seconds=window)
            ]

            if len(request_history[ip_address]) >= limit:
                raise HTTPException(status_code=429, detail="Rate limit exceeded")

            request_history[ip_address].append(now)
            return await func(request, *args, **kwargs)

        return wrapper

    return decorator
