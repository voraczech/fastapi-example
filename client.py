import requests

url = "http://127.0.0.1:8000/zvire/2"

try:
    # Send GET request
    response = requests.get(url)

    # Check if the request was successful
    response.raise_for_status()

    # Parse JSON response
    data = response.json()

    # Print the JSON data
    print("Data retrieved successfully:")
    print(data["zvire"])

    response2 = requests.put("http://127.0.0.1:8000/zvire/bingo")
    response2.raise_for_status()
    data2 = response2.json()
    print(data2["zvire"])

except requests.exceptions.RequestException as e:
    print(f"Request error occurred: {e}")

except ValueError as e:
    print(f"Failed to parse JSON: {e}")
