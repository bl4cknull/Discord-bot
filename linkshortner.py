import pyshorteners

def link_shortner(link):
	shortner = pyshorteners.Shortener()
	x = shortner.tinyurl.short(link)
	return x


