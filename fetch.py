import requests
import os


headers = {"Accept":"application/json", "Content-Type":"application/json", "Authorization":"Bearer token"}
r = requests.get("https://api.spotify.com/v1/playlists/playlist_id", headers=headers)

no_of_tracks = len(r.json()['tracks']['items'])
for i in range(0, no_of_tracks):
	preview_url = r.json()['tracks']['items'][i]['track']['preview_url']
	print(preview_url)
	file_name = r.json()['tracks']['items'][i]['track']['name']+".mp3"
	if preview_url == None:
		pass
	else:
		response = requests.get(preview_url)
		try:
			with open(file_name, 'wb') as f:
				f.write(response.content)
		except Exception as e:
			print(str(e))

