import requests
import time

# Set the URL to which you want to send the POST requests
url = "http://localhost:5000/detect"

# Set the number of requests you want to send
num_requests = 100

# Set the path to the image file you want to send
image_path = "030.jpg"

# Initialize a list to store the response times
response_times = []

# Send the POST requests and time how long it takes to receive the responses
for i in range(num_requests):
    start_time = time.monotonic()
    with open(image_path, 'rb') as image_file:
        response = requests.post(url, files={'image': image_file})
    end_time = time.monotonic()
    response_time = end_time - start_time
    response_times.append(response_time)
    print(f"Request {i+1} took {response_time:.2f} seconds")

# Print the total time it took to receive all the responses
total_time = sum(response_times)
print(f"\nReceived {num_requests} responses in {total_time:.2f} seconds")
