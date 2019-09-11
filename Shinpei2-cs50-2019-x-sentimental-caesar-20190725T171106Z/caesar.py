from cs50 import get_string
import sys
argv = sys.argv

# If the number of command-line arguments isn't three , then finish the program.
if len(argv) != 2:
    print("Usage: python caesar.py k")
    sys.exit(1)


# If the key isn't non-negative number , then finish the program.
# 0以上の数字でなければ、強制終了
if argv[1].isnumeric() is not True or argv[1] == '0':
    print("Usage: python caesar.py k")
    sys.exit(2)

# keyの格納
key = int(argv[1])

# input plaintext
plain = get_string("plaintext: ")
textLen = len(plain)
# create cipher text
cipher = []
cipherText = ""
for i in range(textLen):
    preAscii = ord(plain[i])        # ''で囲むと文字列と認識される点に注意
    newAscii = ord(plain[i])

    if ord('A') <= preAscii <= ord('Z'):
        newAscii = (preAscii + key - ord('A')) % 26 + ord('A')
        # print("uppercase")
    if ord('a') <= preAscii <= ord('z'):
        newAscii = (preAscii + key - ord('a')) % 26 + ord('a')
        # print("lowercase")
    cipher.append(chr(newAscii))
    cipherText += cipher[i]
print("ciphertext:", cipherText)

