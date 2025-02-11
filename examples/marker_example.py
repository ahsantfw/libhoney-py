from libhoney.client import Client
import os
import logging
from dotenv import load_dotenv
load_dotenv()
# Enable debug logging
logging.basicConfig(level=logging.DEBUG)

def main():
    api_key = "1lTEutwsx8n05Jzhb9RdJA" #os.getenv("HONEYCOMB_CONFIG_KEY")
    client = Client(
        writekey=api_key,
        dataset="MyCodeExerciseDataset",
        debug=True  # Enable SDK's debug mode
    )
    
    try:
        # Create a marker (matching the curl example)
        response = client.create_marker(
            dataset="MyCodeExerciseDataset",
            message="deploy #123",  # Using exact same message as curl example
            marker_type="deploy"    # Using exact same type as curl example
        )
        print("Response:", response)

        if isinstance(response, dict) and 'id' in response:
            print("\nMarker created successfully!")
            print(f"Marker ID: {response['id']}")
    
    finally:
        client.close()

if __name__ == "__main__":
    main() 