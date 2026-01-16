import requests

def fetch_and_display_users(num_users):
    
    url = "https://jsonplaceholder.typicode.com/users"
    
    try:
        response = requests.get(url, timeout=5)  # 5-second timeout for network issues
        response.raise_for_status()  # Raises HTTPError for non-200 responses

        users = response.json()  # Parse JSON

        if not isinstance(users, list):
            print("Error: Unexpected JSON structure")
            return None

        # Limit number of users to the available length
        num_to_show = min(num_users, len(users))

        for i in range(num_to_show):
            try:
                user = users[i]
                name = user.get("name", "N/A")
                email = user.get("email", "N/A")
                city = user.get("address", {}).get("city", "N/A")

                print(f"User {i + 1}:")
                print(f"  Name: {name}")
                print(f"  Email: {email}")
                print(f"  City: {city}")
                print("-" * 30)

            except Exception as e:
                print(f"Error processing user {i}: {e}")

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
        return None
    except ValueError as e:
        print(f"Error parsing JSON: {e}")
        return None


# ----------- Example usage -----------

print("Fetching 3 users:\n")
fetch_and_display_users(3)

print("\nFetching 15 users (more than available):\n")
fetch_and_display_users(15)