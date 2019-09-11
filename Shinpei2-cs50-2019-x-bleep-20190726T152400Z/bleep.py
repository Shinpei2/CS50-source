from cs50 import get_string
import sys

argv = sys.argv


def main():
    # CL引数が2以外の場合は終了
    if len(argv) != 2:
        print("Usage: python bleep.py dictionary")
        exit(1)

    # ファイルの読み込み
    file = open(argv[1], "r")

    # リストbanListにbanned.textの文字列を格納する
    banList = []
    for line in file:
        banList.append(line.rstrip("\n"))
    # print(banList)
    file.close()

    # メッセージ入力およびリストへの格納
    message = get_string("What message would you like to censor?\n")
    wordList = message.split()
    # print(message)

    ### lowerWordListの各単語が禁止文字に入ってるかを確認 ###

    # 禁止文字列と比較するために、文字列を小文字に変換
    lowerMessage = message.lower()
    lowerWordList = lowerMessage.split()
    # print(lowerWordList)

    # 禁止文字に該当するlowerWordList内の文字列の添え字を格納
    bIndex = []
    for i in range(len(lowerWordList)):
        for j in range(len(banList)):
            if lowerWordList[i] == banList[j]:
                bIndex.append(i)
                break
    # print(bIndex)

    ### messageの文字列を'*'に変換 ###
    for i in range(len(bIndex)):
        # '*'の個数を確認＋変換後の文字列作成
        wordLen = len(lowerWordList[bIndex[i]])
        cipher = ""
        for j in range(wordLen):
            cipher += "*"
        # print(cipher)

        # message内の該当文字列をcipherで置き換える
        message = message.replace(wordList[bIndex[i]], cipher)
        # print(message)

    # 変換後のmessageの表示
    print(message)


if __name__ == "__main__":
    main()
