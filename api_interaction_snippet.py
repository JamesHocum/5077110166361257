# Example API Interaction (Conceptual)

import requests
import json

API_ENDPOINT = "https://api.example.com/ai"  # Replace with your API endpoint

def call_ai_api(prompt, api_key):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}", # Secure API key
    }
    data = {
        "prompt": prompt,
    }
    try:
        response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API Request failed: {e}")
        return None

# Example usage:
def main():
    api_key = input("Enter your API key: ")
    prompt = input("Enter your prompt: ")
    response = call_ai_api(prompt, api_key)
    if response:
        print("AI Response:")
        print(response.get("response", "No response")) # Safely access the response