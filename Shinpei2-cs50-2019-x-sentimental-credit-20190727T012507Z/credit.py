from cs50 import get_string


# numberを取得する関数
def get_Number():
    while True:
        number = get_string("Number: ")
        if number.isnumeric():
            if int(number) > 0:
                return number


# checkSumを調べる関数
def checkSum(number, digit):
    cSum = 0
    check = 1
    # チェックサムの計算
    for i in range(digit):
        checkDigit = digit - i - 1
        num = 0
        # 後ろから奇数番目
        if check % 2 == 1:
            num = int(number[checkDigit])
        # 後ろから偶数番目
        else:
            num = int(number[checkDigit]) * 2
        check += 1

        # numが10以上の場合
        if num >= 10:
            cSum += num % 10
            num = num // 10
            cSum += num
        # 10未満の場合
        else:
            cSum += num

    # print(cSum)

    # チェックサム判定
    if cSum % 10 == 0:
        return True
    else:
        return False


def main():
    number = get_Number()

    # numberListとdigitの用意
    numberList = []
    digit = len(number)

    ### チェックサムの判定 ###
    # 桁数が13or15or16の場合
    if digit == 13 or digit == 15 or digit == 16:
        # numberの各桁の文字をnumberListへ格納
        for i in range(2):
            numberList.append(number[i])
        # print(numberList)

        ### クレジットカード会社判定 ###
        # AMEX
        if numberList[0] == '3' and numberList[1] == '4' or numberList[1] == '7' and digit == 15:
            if checkSum(number, digit):
                print("AMEX")
            else:
                print("INVALID")

        # MASTERCARD
        elif numberList[0] == '5' and numberList[1] == '1' or numberList[1] == '2' or numberList[1] == '3' or numberList[1] == '4' or numberList[1] == '5' and digit == 16:
            if checkSum(number, digit):
                print("MASTERCARD")
            else:
                print("INVALID")

        # VISA
        elif numberList[0] == '4' and digit == 13 or digit == 16:
            if checkSum(number, digit):
                print("VISA")
            else:
                print("INVALID")

        # それ以外は無効
        else:
            print("INVALID")
    # それ以外の桁数は無効
    else:
        print("INVALID")


if __name__ == "__main__":
    main()