#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <stdlib.h>

int checkDigit(long number);
bool Luhn(long number);

int main(void)
{       
    //カード番号を入力(Luhnチェックが真の場合のみ、カード会社を探索)
    long number = get_long("Number: ");
    if (Luhn(number))
    {
        //カード番号の桁数を取得
        int len = checkDigit(number);
        //printf("len:%i\n",len);
        

        //1桁目、2桁目をdigit[0],digit[1]に]格納
        int digit[2];
        long value = number;
        for (int i = 1; i < len - 1; i++)
        {
            value /= 10;
        }
        digit[1] = value % 10;
        value /= 10;
        digit[0] = value % 10;
    
        //printf("1桁目：%d\n",digit[0]);
        //printf("2桁目：%d\n",digit[1]);
    
        //カード番号の1桁目をチェック
        switch (digit[0])
        {
            //AMEXかどうかを調べる。
            case 3:
                if (len == 15 && (digit[1] == 4 || digit[1] == 7))
                {
                    printf("AMEX\n");
                    break;
                }
                printf("INVALID\n");
                break;
              
            case 4:
                if (len == 13 || len == 16)
                {
                    printf("VISA\n");
                    break;
                }
                printf("INVALID\n");
                break;
            case 5:
                if (len == 16 && (1 <= digit[1] && digit[1] <= 5))
                {
                    printf("MASTERCARD\n");
                    break;
                }
                printf("INVALID\n");
                break;
            default:
                printf("INVALID\n");
                break;
        }
    }
    else
    {
        printf("INVALID\n");
    }
}

//カード番号の桁数を調べる関数chckDigit()
int checkDigit(long number)
{
    int digit = 0;
    while (number != 0)
    {
        number = number / 10;
        digit += 1;
    }
    return digit;
}

//クレジットカードの有効/無効を調べる関数Luhn
bool Luhn(long number)
{
    int len = checkDigit(number);
    int odd = 0;
    int even = 0;
    int checkSum = 0;

    //桁数が偶数の場合
    if (len % 2 == 0)
    {
        for (int i = 0; i <= len / 2; i++)
        {
            odd = number % 10;
            number /= 10;
            even = (number % 10) * 2;
            //偶数番目の桁が10以上の場合に変換
            if (even >= 10)
            {
                even = (even % 10) + ((even / 10) % 10);
            }
            checkSum += odd + even;
            number /= 10;
        }
    }
    
    //桁数が奇数の場合
    else
    {
        //最高桁以外のチェックサム合計を計算
        for (int i = 0; i <= len / 2; i++)
        {
            odd = number % 10;
            number /= 10;
            even = (number % 10) * 2;
            //偶数番目の桁が10以上の場合に変換
            if (even >= 10)
            {
                even = (even % 10) + ((even / 10) % 10);
            }
            checkSum += odd + even;
            number /= 10;
        }
        
        //最高位をチェックサムに加算
        checkSum += number % 10;
    }
    
    //printf("checkSum: %i\n",checkSum);
    
    //checkSumが、10で割り切れる場合：true / 割り切れない場合：false
    if (checkSum % 10 == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}
