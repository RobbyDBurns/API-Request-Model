# API-Request-Model
To showcase knowledge of and explore the applications and implications of the API in a backend setting, specifically with FastAPI.


Virtual Environment:
python3 -m venv venv 

CURL COMMANDS:

curl -X POST http://127.0.0.1:8000/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice", "age": 30}'

curl -X POST -H "Content-Type: application/json" 'https://127.0.0.1:8000/items?item=apple'
