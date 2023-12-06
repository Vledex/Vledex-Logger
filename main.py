import requests

def send_data_and_image_to_webhook(webhook_url, data, image_url):
    try:
        # Download the image
        image_response = requests.get(image_url)
        image_data = image_response.content

        # Include image data in the payload
        data["image_data"] = image_data

        # Send data and image to the webhook
        response = requests.post(webhook_url, json=data)

        if response.status_code == 200:
            print("Data and image sent successfully to the webhook")
        else:
            print(f"Failed to send data and image to the webhook. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print('An error occurred during the request:', str(e))
    except Exception as e:
        print('An unexpected error occurred:', str(e))

# Prompt the user to input the webhook URL, image URL, and data
webhook_url = input("Enter the webhook URL: ")
image_url = input("Enter the image URL: ")
username = input("Enter your username: ")
password = input("Enter your password: ")
additional_data = input("Enter additional data: ")

# Prepare data for the webhook
payload = {
    "username": username,
    "password": password,
    "additional_data": additional_data
}

# Send data and image to the webhook
send_data_and_image_to_webhook(webhook_url, payload, image_url)
