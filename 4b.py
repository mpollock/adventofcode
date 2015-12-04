#given ckczppom, find decimal number to prepend that hashes to 
# something starting with five zeroes

import hashlib

start = "ckczppom"
append = 117946 #ending point of five zeroes
while hashlib.md5(start + str(append)).hexdigest()[:6] != "000000":
	append += 1
print append
