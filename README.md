# Rate Limiting Middleware - Django

## Description
A custom Django middleware that enforces rate-limiting based on IP address. Each IP is limited to 100 requests per rolling 5-minute window.

## How to Run

1. Clone repo / unzip
2. Create virtual environment:
3. Install Django:
4. Run server:
5. Test:

## How to Test

Run the unit tests:
 - python manage.py test

You should see the 101st request return HTTP 429. 
 - Screenshot attached as `test_results.png`


## Test the /test/ endpoint
- http://127.0.0.1:8000/test/

## Features

- Rolling window of 5 minutes
- Uses Django’s built-in cache
- Adds `X-RateLimit-Remaining` header

## Documentation Resources Used:
   - Official Django docs
   - Redis + Django cache documentation