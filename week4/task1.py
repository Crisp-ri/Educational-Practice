import requests

# GET-запит
get_response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(get_response.status_code)
print(get_response.headers)
print(get_response.text)

# POST-запит
data = {
    "title": "test",
    "body": "hello",
    "userId": 1
}

post_response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=data
)

print(post_response.status_code)
print(post_response.headers)
print(post_response.text)
