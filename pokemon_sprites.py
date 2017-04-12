import requests
import json

sprites = {}

# for i in range(1, 251+1):
# 	r = requests.get("http://pokeapi.co/api/v2/pokemon-form/{}/".format(i))
# 	url = r.json()["sprites"]["front_default"]
# 	print(url)
# 	sprites["id{}".format(i)] = {"url": str(url)}

for i in range(1, 251+1):
	s = "http://assets-5.bostonpogomap.com/images/poke/{}.png".format(i)
	# s = "http://serebii.net/pokemongo/pokemon/{:03d}.png".format(i)
	sprites["id{}".format(i)] = { "url":s }

s = json.dumps(sprites, indent=4)

with open("poke_sprites.json", 'w') as f:
	f.write(s)

