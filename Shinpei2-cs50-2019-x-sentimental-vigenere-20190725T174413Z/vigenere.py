from cs50 import get_string
import sys
argv = sys.argv

# If the number of command-line arguments isn't three , then finish the program.
if len(argv) != 2:
    print("Usage: python caesar.py k")
    sys.exit(1)


# 全ての文字が英字でない場合は強制終了
if argv[1].isalpha() is not True:
    print("Usage: python caesar.py k")
    sys.exit(1)

# input plaintext
plain = get_string("plaintext: ")
textLen = len(plain)

# keyの準備
key = 0
keyText = argv[1].upper()       # key文字列を大文字にして変数keyTextに格納
keyCount = 0
keyLen = len(keyText)
keyNum = 0

# create cipher text
cipherText = ""
for i in range(textLen):
    # keyの設定
    keyNum = keyCount % keyLen
    key = ord(keyText[keyNum]) - ord('A')

    # 変換前後のAscii値を変数に格納
    preAscii = ord(plain[i])        # ''で囲むと文字列と認識される点に注意
    newAscii = ord(plain[i])

    # 文字が大文字である場合の処理
    if ord('A') <= preAscii <= ord('Z'):
        newAscii = (preAscii + key - ord('A')) % 26 + ord('A')
        # print("uppercase")
        # keyCountを次に進める
        keyCount += 1

    # 文字が小文字である場合の処理
    if ord('a') <= preAscii <= ord('z'):
        newAscii = (preAscii + key - ord('a')) % 26 + ord('a')
        # print("lowercase")
        # keyCountを次に進める
        keyCount += 1

    # 変換処理後の文字をcipehrtextに追加
    cipherText += chr(newAscii)

# ciphertextを出力
print("ciphertext:", cipherText)
