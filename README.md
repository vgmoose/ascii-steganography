# ascii-steganography
Hide files and data in plain ascii text that is invisible to the naked eye.

### Background
Ascii contains some unused bytes that are not rendered in most applications. More often than not, these bytes are not striped out and persist even through posting to websites or copy and pasting plaintext. Data can be encoded into a special format that is made up exclusively of these unused bytes, which allow it to be hidden and unrendered, yet still transferrable.

See the sections below for more information on how this works.

### Storing / Encoding
Running the below code on a file will embed /path/to/file/to/encode.file into "text that you want to encode" and save the result to output.txt in the same directory.
```
git clone https://github.com/vgmoose/ascii-steganography.git
cd ascii-steganography
python data.py
store
/path/to/file/to/encode.file
text that you want to encode
```
Once output.txt is generated (hopefully successfully) it can be opened in any text editor (terminal based ones tend to render the unused bytes, so use a GUI based one if possible) and sent to the clipboard for copying. The hidden data is spliced directly into the middle of the string.

### Extracting / Decoding
Running the code below will extract hidden content from output.txt. This is a text document that contains a pasted ascii string with hidden content. Again, this is recomended to be done in a GUI application rather than a terminal.
```
git clone https://github.com/vgmoose/ascii-steganography.git
cd ascii-steganography
python data.py
extract
output.txt
```
A good candidate file to run the extract on is (obviously) the output of the storing operation. The hidden file will be extracted to the current directory under the same filename that it was under when it was stored. The file should be bytewise the same as it was when it was encoded, and if it is not, please file an Issue on Github.

### Caveats
Due to the limited number of unused bytes in ascii, there is a 2x overhead for every file that is encoded. Whatever you copy and paste will be this large filesize, so if posting to the Internet, smaller files are recommended to be encoded.

Additionally, no security is provided besides being invisible to the user. Someone inspecting the data would know immediately that more than plaintext was present. However, if the original file was encrypted first, the hidden data would still be secret, despite it being obvious that it was hidden.

### How it Works

#### File format
If the original text was "Hello there's nothing hidden in this message." and the hidden file was an image named "hidden.jpg", the resulting output.txt would look like this (with the hidden data in brackets):
```
Hello there's nothing hidd[delimiter][encoded filename hidden.jpg][delimiter][encoded image bytes][delimiter]en in this message.
```
The reason the data is written to a file is so that it is easier to copy and paste, as a Terminal often renders the unused bytes. The intent is not to upload the file, but rather to use the plaintext within the file.

#### Charset
The current version of ascii-steganography uses the following charset:

Ascii Value   | Intended Use (unused) | Steganography value (nibble) 
------------- | ------------- | ------------- 
0x01 | Start of Heading | 0x0
0x02 | Start of Text | 0x1
0x03 | End of Text | 0x2
0x04 | End of Transmission|0x3
0x05 | Enquiry|0x4
0x06 | Acknowledge|0x5
0x07 | Bell|0x6
0x0E | Shift Out|0x7
0x0F | Shift In|0x8
0x10 | Data Link Escape|0x9
0x11 | Device Control 1|0xA
0x12 | Device Control 2|0xB
0x13 | Device Control 3|0xC
0x14 | Device Control 4|0xD
0x15 | Negative Acknowledge|0xE
0x16 | Synchronous Idle|0xF
0x19 | End of Medium|Delimiter

The charset may be updated to use characters that are less likely to be striped out or used in popular applications. Any 16 characters can be used for the nibble, and then one more for the delimiter. Each unused byte makes up half of an encoded byte of the hidden data.

### Web app
Coming soon to make ascii-steganography easier to use and more accessible for average users.
