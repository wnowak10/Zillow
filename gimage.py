import streetview
panoids = streetview.panoids(lat=-33.85693857571269, lon=151.2144895142714)

direc = './' # where to put image. put in current working dir
panoid = panoids[0]['panoid'] # get first image from this location
heading = 0 # see docs for info on this. controls which direction we're looking
flat_dir = direc
key = secrets.key

r = streetview.api_download(panoid, heading, flat_dir, key)
