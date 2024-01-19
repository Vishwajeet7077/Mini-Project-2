import requests

base_url = 'http://127.0.0.1:8000/api/get_rate'  
company_name = input("Enter Name: ")

# Construct the URL by appending the company name to the base URL
url = f'{base_url}{company_name}/'

try:
    response = requests.get(url)

    # Check the response status code
    if response.status_code == 200:
        # Assuming the response contains JSON data, you can parse it
        data = response.json()

        # Extract the rate from the JSON response
        rate = data.get('rate')

        if rate is not None:
            print(f"Rate for {company_name}: {rate}")
        else:
            print("Rate not found in the response data.")
    else:
        print(f"Request failed with status code {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Request exception: {e}")
