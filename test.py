import requests

def fetch_data_from_backend():
    try:
        # Make a GET request to the Flask server (replace with your actual server address)
        response = requests.get('http://127.0.0.1:5001')
        
        # Check if the response is successful
        if response.status_code == 200:
            data = response.json()  # Parse the JSON response
            print("Data from backend:")
            for city in data:
                print(f"- {city['name']}")  # Print the city name from the list
        else:
            print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Call the function to fetch the data
fetch_data_from_backend()
