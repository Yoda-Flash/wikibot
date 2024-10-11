# import os
# import requests
# from dotenv import load_dotenv
#
# load_dotenv()
# APP_ID = os.getenv("APP_ID")
# TOKEN = os.getenv("DISCORD_TOKEN")
#
# url = f"https://discord.com/api/v10/applications/{APP_ID}/commands"
#
# test = {
#   "name": "test",
#   "type": 1,
#   "description": "Press for magic to happen"
# }
#
# headers = {
#   "Authorization": f"Bot {TOKEN}"
# }
#
# r = requests.post(url, headers=headers, json=test)