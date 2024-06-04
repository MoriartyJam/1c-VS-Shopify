import requests
from requests.auth import HTTPBasicAuth
import json

# URL to fetch the products
url = "http://207.180.219.163:65180/floristics/hs/Post/v1/GetAllItemsShopify"

# Basic authentication credentials
username = "web"
password = "Ufpc4405"

# Example payload (modify according to the API's requirements)
payload = {}


def fetch_products():
    try:
        # Send POST request with basic authentication and payload
        response = requests.post(url, auth=HTTPBasicAuth(username, password), json=payload)

        # Check if the request was successful
        if response.status_code == 200:
            # Decode response content using utf-8-sig to handle BOM
            content = response.content.decode('utf-8-sig')
            # Parse JSON response
            products = json.loads(content)
            return products
        else:
            print(f"Failed to fetch products. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def main():
    products = fetch_products()
    if products:
        print("Products fetched successfully:")
        print(products)
    else:
        print("No products found or an error occurred.")


if __name__ == "__main__":
    main()