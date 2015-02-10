import os

keys = [0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0xE, 0xF, 0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16]

term = 0x19

def decrypt(data):
	output = ""
	nextwrite = False
	bytesofar = 0
	for b in bytes(data):
		n = keys.index(ord(b))
		if not nextwrite:
			bytesofar = n << 4
			nextwrite = True
		else:
			bytesofar += n
			nextwrite = False
			output += chr(bytesofar)

	return output


def encrypt(data):
	output = ""
	for b in bytes(data):
		n1 = ord(b) & 0xF
		n2 = ord(b) >> 4
		output += chr(keys[n2])
		output += chr(keys[n1])
	
	return output

ans = raw_input("[s]tore or [e]xtract? ")
if ans[0].lower() == "s":
	data = raw_input("path to file to store? ").replace("\\","").strip()
	plain = raw_input("text to encode? ").strip()
	f = open(data, "r")
	f3 = open("output.txt", "w+")
	name = os.path.basename(data)
	data = f.read()
	half = int(len(plain)/2.0)
	f3.write(plain[:half] + chr(term) + encrypt(name) + chr(term) + encrypt(data) + chr(term) + plain[half:])
	print "Encoded string saved to output.txt"

elif ans[0].lower() == "e":
	data = raw_input("path to file to extract? ").replace("\\","").strip()
	f = open(data, "r")
	data = f.read()
	packets = data.split(chr(term))
	name = decrypt(packets[1])
	contents = decrypt(packets[2])

	f2 = open(name, "w+")
	f2.write(contents)
	print "Decoded data saved to " + name

else:
	print "ok wise guy"
