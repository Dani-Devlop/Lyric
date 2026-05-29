#from azapi import AZlyrics

# Names should be passed corrrectly
# If you can't remember, use google or duckduckgo
# AZlyrics('google')
#api = AZlyrics()

#api.artist = "Taylor Swift"
#api.title = "Blank Space"

#api.getLyrics(save=True)

#################################

import json
from musicxmatch_api import MusixMatchAPI

api = MusixMatchAPI()

try:
    search = api.search_tracks("skyfall")
    print("--- Success! ---")
    print(json.dumps(search, indent=4))
except Exception as e:
    print(f"--- Error Occurred: {e} ---")
    
    # Inspect the last response directly from the underlying session
    if hasattr(api, 'session') and api.session:
        last_response = getattr(api, 'last_response', None)
        if last_response:
            print(f"\nStatus Code: {last_response.status_code}")
            print("Raw Response Text (first 500 chars):")
            
#print(json.dumps(search, indent=4)))


