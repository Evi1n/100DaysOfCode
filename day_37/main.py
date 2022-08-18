import requests
from datetime import datetime

USERNAME = "yournusername"
TOKEN = "yourtoken"
GRAPHID = "yourgraphid"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor" : "yes",
}

# POST
#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

#---------- Graphic Creation -----------#

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPHID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN" : TOKEN,
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

#---------- Pixel Creation ----------#
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"
today = datetime.now()
edited_date = today.strftime("%Y%m%d")
pixel_data = {
    "date": edited_date,
    "quantity": input("How many kilometers did you cycle today?"),
}

#response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
#print(response.text)

#---------- Update Pixel ----------#

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{edited_date}"
update_pixel_data = {
    "quantity": "34",
}

# PUT
#response = requests.put(url=update_endpoint, json=update_pixel_data, headers=headers)
#print(response.text)

#---------- Delete Pixel ----------#

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{edited_date}"

# DELETE
#response = requests.delete(url=delete_endpoint, headers=headers)
#print(response.text)