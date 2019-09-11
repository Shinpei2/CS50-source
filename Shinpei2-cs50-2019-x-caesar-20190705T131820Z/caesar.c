#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int main(int argc, string argv[])
{
    //コマンドライン引数の個数が2以外の場合、強制終了。
    if (argc != 2)
    {
        printf("Usage: ./ key\n");
        return 1;
    }

    
    //引数の文字が数字以外の場合、強制終了
    for (int i = 0, charLen = strlen(argv[1]); i < charLen; i++)
    {
        if (!(isdigit(argv[1][i])))
        {
            printf("Usage: ./ key\n");
            return 1;
        }
    }
    int keyNum = atoi(argv[1]);
    
    //printf("Success\n");
    //printf("%i\n",keyNum);
    
    //平文の入力、出力
    printf("plaintext: ");
    string plainText = get_string("");
    
    //暗号文の表示
    printf("ciphertext: ");
    for (int i = 0, textLen = strlen(plainText); i < textLen; i++)
    {
        int asciiNum = plainText[i];
        
        //大文字、または小文字であれば暗号化
        if ('A' <= asciiNum && asciiNum <= 'Z')
        {
            asciiNum = (plainText[i] + keyNum - 'A') % 26 + 'A';
        }
        else if ('a' <= asciiNum && asciiNum <= 'z')
        {
            asciiNum = (plainText[i] + keyNum - 'a') % 26 + 'a';
        }
        
        //i番目の文字を表示
        printf("%c", asciiNum);
    }
    printf("\n");
}
