keyText = "ace"
key = 0
keyNum = 0
keyCount = 0
keyLen = len(keyText)

for i in range(20):
    keyNum = keyCount % keyLen
    key = ord(keyText[keyNum]) - ord('a')
    print(key)
    keyCount += 1