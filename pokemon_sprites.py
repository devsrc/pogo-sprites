import requests
import json
import urllib
from os.path import join


sprites = {}
outfile = "poke_sprites.json"
source_url_base = "http://assets-5.bostonpogomap.com/images/poke/"
poke_ids = range(1, 251+1)

for i in poke_ids:
	fname = "{}.png".format(i)
	s = "{}{}".format(source_url_base, fname)

	try:
		t = urllib.urlretrieve(s, join("sprites", "clean", fname))
	except IOError:
		print("Error at id: {}".format(i))

	sprites["id{}".format(i)] = { "url":s }

with open(outfile, 'w') as f:
	f.write(json.dumps(sprites, indent=4))

