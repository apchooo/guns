import requests
import time
from concurrent import futures

url = "http://localhost:8000/detect"
num_requests = 100
image_path = "030.jpg"

def send_request(image_path):
    with open(image_path, 'rb') as image_file:
        response = requests.post(url, files={'image': image_file})
    return response

start_time = time.monotonic()

# Use ThreadPoolExecutor with a fixed number of workers to send multiple requests concurrently
with futures.ThreadPoolExecutor(max_workers=2) as executor:
    # Submit the requests to the executor
    future_responses = [executor.submit(send_request, image_path) for _ in range(num_requests)]

# Collect the responses
responses = [future.result() for future in future_responses]

end_time = time.monotonic()
total_time = end_time - start_time

print(f"Received {num_requests} responses in {total_time:.2f} seconds")
