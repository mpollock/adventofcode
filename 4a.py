#given ckczppom, find decimal number to prepend that hashes to 
# something starting with five zeroes

import hashlib

start = "ckczppom"
append = 1
while hashlib.md5(start + str(append)).hexdigest()[:5] != "00000":
	append += 1
print append
