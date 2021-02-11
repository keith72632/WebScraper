import requests #module for SIMPLE requests from browers

#fetches info from url
response = requests.get('https://automatetheboringstuff.com/files/rj.txt')
#raise_for_status will interupt program if there is an issues connecting to url
response.raise_for_status()

fd = open('RomeoandJulio.txt', 'wb')

#.iter_content iterates over content from url
for chunk in response.iter_content():
	fd.write(chunk)



