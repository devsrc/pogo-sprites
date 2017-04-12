import requests
import json
import urllib
from os.path import join


sprites = {}
outfile = "poke_sprites.json"
source_url_base = "https://assets-5.bostonpogomap.com/images/poke/"
target_url_base = "https://raw.githubusercontent.com/devsrc/pogo-sprites/master/sprites/clean/"
poke_ids = range(1, 251+1)

for i in poke_ids:
	fname = "{}.png".format(i)
	s = "{}{}".format(target_url_base, fname)
	sprites["id{}".format(i)] = { "url":s }

with open(outfile, 'w') as f:
	f.write(json.dumps(sprites, indent=4))

